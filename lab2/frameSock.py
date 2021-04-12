"""
Abram Nguyen

A socket is an endpoint in a 2-way communication 
link between two programs running on a network.
It may send or receive files.
"""

import socket

class frameSock:
    def __init__(self, socket):
        self.sock = socket
        self.buff = "".encode()
        self.limit = 100

    """
    Given a string 'msg', send 'msg' in manageable pieces
    using a buffer.
    """
    def send_msg(self, msg):
        last_byte = 0 # index in byte array
        byte_arr = str(len(msg)).encode + b':' + msg.encode() # out-of-band framing; "5:hello"
        new_msg = "" # message to be taken from buffer

        while len(byte_arr) != 0:
            last_byte = self.socket.send(byte_array) # send byte array, looks like [2,:,m,e]
            new_msg += byte_arr[:last_byte].decode() # get bytes from array into a string 'new_msg'
            byte_arr = byte_arr[last_byte:] # next byte

        return new_msg


    """
    Attempt to receive a number of bytes (below limit) from buffer
    and return a complete message.
    """
    def recv_msg(self):
        if len(self.buff) == 0: #nothing in buffer? try receiving
            self.buff = self.socket.recv(self.limit).decode() # recv bytes under limit (max)
            msg_start = self.buff.index(':') # message looks like "5:hello"
            msg_len = int(self.buff[:msg_start]) # find msg len from buffer? use [:] array notation
            self.buff = self.buff[msg_start+1:] # buff now contains text, without ":"

            msg = ""
            while len(msg) != msg_len:
                if len(self.buff) == 0: #nothing in buffer? try receiving
                    self.buff = self.socket.recv(self.limit).decode()
                msg += self.buff[0] # receive 1 char at a time from buff
                self.buff = self.buff[1:] # essentially remove char from buff (already received)

            return msg
