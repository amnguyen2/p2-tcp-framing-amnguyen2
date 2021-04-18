"""
Abram Nguyen
"""
#! /usr/bin/env python3

# Echo server program

import socket, sys, re, os
sys.path.append("../lib")       # for params
import params, frameSock
import workThread

switchesVarDefaults = (
    (('-l', '--listenPort') ,'listenPort', 50001), # server listens at localhost 50001
    (('-?', '--usage'), "usage", False), # boolean (set if present)
    )

paramMap = params.parseParams(switchesVarDefaults)

listenPort = paramMap['listenPort']
listenAddr = ''       # Symbolic name meaning all available interfaces

if paramMap['usage']:
    params.usage()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((listenAddr, listenPort))
sock.listen(1)              # allow only one outstanding request
# s is a factory for connected sockets

while True:
    connectedSock, addr = sock.accept() # wait until incoming connection request (and accept it)
    workThread.workThread(connectedSock, addr).start()

"""
    if os.fork() == 0:      # child becomes server
        print('Connected by', addr)
        connectedSock.send(b"hello")
        connectedSock.send(b"world")
        connectedSock.shutdown(socket.SHUT_WR)
"""

