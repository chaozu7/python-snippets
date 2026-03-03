#implement a program that expects exactly one command-line argument, the name (or path) of a Python file,
# and outputs the number of lines of code in that file, excluding comments and blank lines. If the user does not specify exactly one command-line argument,
# or if the specified file’s name does not end in .py, or if the specified file does not exist, the program should instead exit via sys.exit.
#
#

import sys

def main():
    getFile()

def getFile():
    i = 0
    if len(sys.argv) == 2:
        fileName = sys.argv[1]
        if fileName.endswith('.py'):
            try:
                with open(fileName) as file:
                    for line in file:
                        lineStrip = line.lstrip(' ')
                        if lineStrip.startswith('#') or len(lineStrip) == 1:
                            i = i
                        else:
                            i+=1
                print(i)

            except FileNotFoundError:
                sys.exit('no such file')
        else:
            sys.exit('wrong type')

    elif len(sys.argv) > 2:
        sys.exit('to many arguments')
    else:
        sys.exit('to few arguments')


main()
