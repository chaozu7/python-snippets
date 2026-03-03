import csv
import sys
from tabulate import tabulate

def main():
    getFile()

def getFile():

    if len(sys.argv) == 2:
        fileName = sys.argv[1]
        if fileName.endswith('.csv'):
            try:
               f = open(fileName)
               elements = []
               with f as file:
                   reader = csv.reader(file)
                   for row in reader:
                       elements.append(row)
               print(tabulate(elements, headers="firstrow", tablefmt="grid"))
            except FileNotFoundError:
                sys.exit('File does not exist')
        else:
            sys.exit('Not a CSV file')

    elif len(sys.argv) > 2:
        sys.exit('too many arguments')
    else:
        sys.exit('too few arguments')


main()
