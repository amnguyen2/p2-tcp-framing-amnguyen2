"""
Abram Nguyen

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

"""
paramMap = params.parseParams(switchesVarDefaults)
server, usage  = paramMap["server"], paramMap["usage"]

if usage:
    params.usage()
"""

if sys.argv[0] == "send":
    try:
        localFile = sys.argv[1]
        serverHost, remoteFile = re.split(":", sys.argv[2])
        serverPort = 50001
        print(serverHost)
        print(remoteFile)
    except:
        print("Something went wrong.")
        print(sys.argv[1])
        print(sys.argv[2])
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
"""
delay = float(paramMap['delay']) # delay before reading (default = 0s)
if delay != 0:
    print(f"sleeping for {delay}s")
    time.sleep(delay)
    print("done sleeping")


print("Zero length read. Closing")
s.close()
"""
framed_sock = frameSock.frameSock(sock)
sent = framed_sock.send_msg('send')
os.write(1, ("Sending " + sent + '!\n').encode())

sent = framed_sock.send_msg(remoteFile)
os.write(1, ("Sending " + sent + '!\n').encode())
"""
while 1:
    data = s.recv(1024). decode()
    print("Received '%s'" % data)
    if len(data) == 0:
        break
"""
response = framed_sock.recv_msg()
os.write(1, ("Receiving " + response + '\n').encode())

if response == "accept":
    data = myReadFile(localFile)
    framed_sock.send_msg(data)
    os.write(1, "Sending " + localFile.encode() + "\n")

    response = framed_sock.recv_msg()
    os.write(1, "Receiving " + response.encode() + "\n")
else:
    os.write(1, "File " + localFile.encode() + " exists.")
sock.close()
