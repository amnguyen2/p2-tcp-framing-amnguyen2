import os, sys, socket, time
from threading import Thread, enumerate
import frameSock

threadNum = 0

class workThread(Thread):
    def __init__(self, connectedSock, addr):
        global threadNum
        Thread.__init__(self, name = "Thread-%d" % threadNum)
        threadNum += 1
        self.connectedSock = connectedSock
        self.addr = addr

    def run(self):
        print("Worker thread running.")
        framed_sock = frameSock.frameSock(self.connectedSock)

        request = framed_sock.recv_msg()
        os.write(1, "Recieving: {} (line20)\n".format(request).encode())
        
        if request == "send":
            file_name = framed_sock.recv_msg()
            os.write(1, "Receiving {}\n".format(file_name).encode())

            path = "./server_data/" + file_name

            if os.path.isfile(path):
                sent = framed_sock.send_msg("This file already exists.")
                os.write(1, "Sending {}\n".format(sent).encode())

            else:
                os.write(1, ("Sending: " + framed_sock.send_msg("accept") + "\n").encode())
                fd = os.open("./server_data/" + file_name, os.O_CREAT | os.O_WRONLY)
                os.write(fd, (framed_sock.recv_msg()).encode())
                os.close(fd)
                os.write(1, "File {} created.\n".format(file_name).encode())
        else:
            os.write(1, "Could not complete request".encode())
        self.connectedSock.shutdown(socket.SHUT_WR)
