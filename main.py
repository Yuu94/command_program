import os

def main():
    global dir
    dir = './'

    while(True):
        command = input('cmd: ')
        commandList = READ(command)
        result = EVAL(commandList)
        PRINT(result)


def READ(command):
    if command in ' ':
        commandList = command.split(' ')
        return commandList
    else:
        return command

def EVAL(command):
    if command == 'ls':
        return LIST()

def PRINT(result):
    resultLen = len(result)
    count = 1

    for p in result:
        if count != 5:
            print(p, " ",end="")
        else:
            print(p)
            count = 1
        count += 1
    
    if resultLen % 5:
        print()


def LIST():
    fileList = os.listdir(dir)
    return fileList

if __name__ == '__main__':
    main()
