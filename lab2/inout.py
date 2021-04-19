import os

# Reads the next line entered by user.

curr = 0
ibuf = ""
sbuf = ""

def myReadLine(fd = 0, limit = 100):
    global curr
    global ibuf
    global sbuf

    if ibuf == "":
        ibuf = os.read(fd,limit)
        sbuf = ibuf.decode()
    line = ""
    while curr < len(sbuf):
        line += sbuf[curr] # adds each character to line
        if sbuf[curr] == '\n': # if character is '\n' return line
            curr += 1
            return line
        curr += 1
        if curr == limit:  # if end of buffer is reached, read again.
            ibuf =  os.read(fd,limit)
            sbuf = ibuf.decode()
            curr = 0

    return ""

def myReadFile(filename):
    fd = os.open(filename, os.O_RDONLY)
    lines = ""
    line = myReadLine(fd)
    while line != "":
        lines += line
        line = myReadLine(fd)
    return lines

"""
import os

inputBuff = 0 # list of chars, used to read max 100 bytes from keyboard 
nextChar = 0 # index of the next char in buff

def myReadFile(fileName):
    print("Reading lines of " + fileName + '\n')
    fd = os.open(fileName, os.O_RDONLY)
    lines = ""
    ln = myReadLine()

    while len(ln) != 0:
        lines += ln
        ln = myReadLine()

    return lines
        
def myReadLine():
    global nextChar, inputBuff
    line = "" # reading line... add chars to line
    
    currChar = myGetChar() # get input char from user keyboard
    while currChar != '' and currChar != "EOF": # while not reached EOF
        line += currChar
        currChar = myGetChar()

    inputBuff = 0
    nextChar = 0

    return line


def myGetChar():
    global nextChar
    global inputBuff

    if nextChar == inputBuff:  # buffer empty
        nextChar = 0
        inputBuff = os.read(0, 100) # (fd 0 is keyboard, num bytes)

        if inputBuff == None: # end of file
            return "EOF"
        
    if nextChar < len(inputBuff) - 1: # still reading input buffer
        strBuff = inputBuff.decode() # .decode(): bytes to chars
        currChar = strBuff[nextChar] # get a char from buffer
        nextChar += 1
        return currChar
    else:
        return "EOF" # reached buffer end

    
def writeLine(line):
    os.write(1, line.encode()) # .encode(): chars to bytes
"""