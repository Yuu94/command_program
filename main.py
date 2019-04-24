import os
import sys

dir = ''
osName = ''
def main():
    global dir
    dir = os.getcwd()

    global osName
    osName = os.name

    print('\nHello User!')

    while(True):
        inputData = input('{} CMD> '.format(dir.split('\\')[-1]))
        command, argument = READ(inputData)
        result = EVAL(command, argument)
        PRINT(result)

def READ(inputData):
    argument = []

    if ' ' in inputData:
        inputList = inputData.split()
        command = inputList[0]

        for i in inputList[1:]:
            argument.append(i)        
    else:
        command = inputData
        argument = None

    return command, argument

def EVAL(command, argument):
    if command == 'ls':
        return LIST()
    elif command == 'dir':
        return LIST()
    elif command == 'cd':
        return ChangeDirectory(argument, osName)
    elif command == 'pwd':
        return PrintWorkingDirectory()
    elif command == 'help':
        return HELP()
    elif command == 'exit':
        return 'exit'
    elif command == '':
        return ''
    else:
        return ERROR('Undefined Command.')

def PRINT(result):
    if result != 'exit':
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
    else:
        print('Good Bye!!')
        sys.exit()



def LIST():
    fileList = os.listdir(dir)
    return fileList

def ChangeDirectory(argument, osName):
    global dir
    if osName == 'nt':
        # Absolute path
        if ':\\' in argument[0]:
            dir = argument[0]
            if '\\\\' in argument[0]:
                dir = dir.replace(mozi, '')            
        # Relative path
        else:
            # ../../../ 対応 split('/')して [.., .., .., hoge]でループ
            if ('..\\' in argument[0]) or ('..' in argument[0]):
                dir = dir.split('\\')[:-1]
                dir.append(argument[0].lstrip('..\\'))
                if dir[-1] == '':
                    dir.pop(-1)
                dir = '\\'.join(dir)
            else:
                dir += '\\' + argument[0]
    try:
        os.listdir(dir)
    except OSError:
        # ERROR('Undedined "{}" Directory.'.format(dir))
        dir = os.getcwd()
        return ERROR('Undedined "{}\\{}" Directory.'.format(dir, argument[0]))
    except:
        return ERROR('Unexpected Error.')
    
    return ''

def PrintWorkingDirectory():
    return [dir]



def HELP():
    print('''-/-/-/-/-/-/-/-/-/-/-HELP-/-/-/-/-/-/-/-/-/-/-
Command Name|   Description
-----------------------------------------
exit        |   command program exit
help        |   print help
cd          |   change directory
ls          |   display current directory
dir         |   display current directory
    ''')

    return ''


def ERROR(message):
    return ['Error: {}'.format(message)]

if __name__ == '__main__':
    main()
