"""
Abram Nguyen

Client communicates with server using requests via sockets
in order to send the contents of a local file.
"""

import socket, sys, re, time, os
sys.path.append("../lib")        # for params
import params
from inout import myReadLine, myReadFile
import frameSock # framed socket class


switchesVarDefaults = (
    (('-s', '--server'), 'server', "127.0.0.1:50001"),
    (('-d', '--delay'), 'delay', "0"),
    (('-?', '--usage'), "usage", False) # boolean (set if present)
    )

if sys.argv[0] == "send":
    try:
        localFile = sys.argv[1]
        serverHost, remoteFile = re.split(":", sys.argv[2])
        serverPort = 50001
    except:
        print("Something went wrong. Enter command:")
        print("python3 client.py send [localFile] [serverHost]:[remoteFile]")
        sys.exit(1)
else:
    sys.exit(1)

    
s = None
for res in socket.getaddrinfo(serverHost, serverPort, socket.AF_UNSPEC, socket.SOCK_STREAM):
    # af = address family
    af, socktype, proto, canonname, sa = res
    try:
        print("creating sock: af=%d, type=%d, proto=%d" % (af, socktype, proto))
        sock = socket.socket(af, socktype, proto)
    except socket.error as msg:
        print(" error: %s" % msg)
        sock = None
        continue
    try:
        print(" attempting to connect to %s" % repr(sa))
        sock.connect(sa)
    except socket.error as msg:
        print(" error: %s" % msg)
        sock.close()
        sock = None
        continue
    break

if sock is None:
    print('could not open socket')
    sys.exit(1)

framed_sock = frameSock.frameSock(sock)
sent = framed_sock.send_msg('send')
os.write(1, ("Sending " + sent + '\n').encode())

sent = framed_sock.send_msg(remoteFile)
os.write(1, ("Sending " + sent + '\n').encode())

response = framed_sock.recv_msg()
os.write(1, ("Receiving " + response + '\n').encode())

if response == "accept":
    print("Reading file named " + localFile + '\n')
    data = myReadFile(localFile)
    framed_sock.send_msg(data)
    os.write(1, "Sending {}\n".format(localFile).encode())

    response = framed_sock.recv_msg()
    os.write(1, "Receiving {} \n".format(response).encode())

sock.close()
