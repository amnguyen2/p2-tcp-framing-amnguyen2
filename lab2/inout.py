import os

currByte = 0
limit = 100 # read 100 bytes at a time
inputBuff = "" # originally bytes, decoded to str into strBuff
strBuff = "" 

def myReadLine(fd = 0):
    global currByte
    global limit
    global inputBuff
    global strBuff

    if inputBuff == "": # input buffer is empty
        inputBuff = os.read(fd,limit) # try reading file again
        strBuff = inputBuff.decode() 
    line = ""
    while currByte < len(strBuff):
        line += strBuff[currByte] # adds each character to line
        if strBuff[currByte] == '\n': # if character is '\n' return line
            currByte += 1
            return line
        currByte += 1
        if currByte == limit:  # if end of buffer is reached, read again.
            inputBuff =  os.read(fd,limit)
            strBuff = inputBuff.decode()
            currByte = 0

    return ""


def myReadFile(file_name):
    fd = os.open(file_name, os.O_RDONLY)
    lines = ""
    line = myReadLine(fd)
    while line != "":
        lines += line
        line = myReadLine(fd)
    return lines
