import sys, socket, time
from threading import Thread, enumerate
import frameSock

threadNum = 0

class workThread(Thread):
    def __init__(self, connectedSock, addr):
        global threadnum
        Thread.__init__(self, name = "Thread-%d" % threadNum)
        threadNum += 1
        self.connectedSock = connectedSock
        self.addr = addr

    def run(self):
        framed_sock = frameSock.frameSock(self.connectedSock)

        request = framed_sock.recv_msg()
        os.write(1, "Receiving " + request.encode() + "\n")

        if request = "send":
            file_name = framed_sock.recv_msg()
            os.write(1, "Receiving " + file_name.encode() + "\n")

            if os.path.isfile("./server_data/" + file_name):
                sent = framed_sock.send_msg("This file already exists.")
                os.write(1, "Sending " + sent.encode() + "\n")

            else:
                os.write(1, ("Sending: " + framed_sock.send_msg("accept") + "\n").encode())
                fd = os.open("./server_data/" + filename, os.O_CREAT | os.O_WRONLY)
                os.write(fd, (framed_sock.recv_msg()).encode())
                os.close(fd)
                os.write(1, ("File {} created.\n").format(fileName).encode())
        else:
            os.write(1, "Could not complete request".encode())
        self.connectedSock.shutdown(socket.SHUT_WR)
