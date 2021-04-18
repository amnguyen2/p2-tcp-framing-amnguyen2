import os

inputBuff = 0 # list of chars, used to read max 100 bytes from keyboard 
nextChar = 0 # index of the next char in buff

def myReadFile(fileName):
    fd = os.open(fileName, os.O_RDONLY)
    lines = ""
    ln = myReadLine()

    while len(line) != 0:
        lines += line
        ln = myReadLine()

    return lines
        
def myReadLine():
    global nextChar, inputBuff
    line = "" # reading line... add chars to line
    
    currChar = myGetChar() # get input char from user keyboard
    while (currChar != '' and currChar != "EOF"): # while not reached EOF
        line += currChar
        currChar = myGetChar()

    inputBuff = 0
    nextChar = 0

    return line


def myGetChar():
    global nextChar
    global inputBuff

    if nextChar == inputBuff:  # buffer empty
        nextChar = 0; 
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
