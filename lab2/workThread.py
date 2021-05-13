import os, sys, socket, time
from threading import Thread, enumerate, Lock
import frameSock

threadNum = 0

lock = Lock()
inUse = set()


class workThread(Thread):
    def __init__(self, connectedSock, addr):
        global threadNum
        Thread.__init__(self, name = "Thread-%d" % threadNum)
        threadNum += 1
        self.connectedSock = connectedSock
        self.addr = addr

    def isFileInUse(self, file_name):
        global lock
        global inUse

        lock.acquire()
        if file_name not in inUse:
            inUse.add(file_name)
            lock.release()
            return True
        
        lock.release()
        return False
        
    def run(self):
        global inUse
        
        print("Worker thread running.")
        framed_sock = frameSock.frameSock(self.connectedSock)

        request = framed_sock.recv_msg()
        os.write(1, "Recieving: {} (line20)\n".format(request).encode())
        
        if request == "send":
            file_name = framed_sock.recv_msg()
            os.write(1, "Receiving {}\n".format(file_name).encode())

            path = "./server_data/" + file_name

            if (self.isFileInUse(file_name) == False):
                framed_sock.send_msg("The file {} is currently in use. Please wait.\n".format(file_name).encode())
                
            elif os.path.isfile(path):
                sent = framed_sock.send_msg("This file already exists.")
                os.write(1, "Sending {}\n".format(sent).encode())

            else:
                os.write(1, ("Sending: " + framed_sock.send_msg("accept") + "\n").encode())
                fd = os.open("./server_data/" + file_name, os.O_CREAT | os.O_WRONLY)
                os.write(fd, (framed_sock.recv_msg()).encode())
                os.close(fd)
                os.write(1, "File {} created.\n".format(file_name).encode())
                
            inUse.remove(file_name) # file has been sent successfully at this point

        else:
            os.write(1, "Could not complete request".encode())

        self.connectedSock.shutdown(socket.SHUT_WR)
