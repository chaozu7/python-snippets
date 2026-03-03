#Expects the user to provide two command-line arguments:
#the name of an existing CSV file to read as input, whose columns are assumed to be, in order, name and house, and
#the name of a new CSV to write as output, whose columns should be, in order, first, last, and house.
#Converts that input to that output, splitting each name into a first name and last name. Assume that each student will have both a first name and last name.
#If the user does not provide exactly two command-line arguments, or if the first cannot be read, the program should exit via sys.exit with an error message.

#
#name = input("What's your name? ")
#home = input("Where's your home? ")

#with open("students2.csv", "a") as file:
#    writer = csv.DictWriter(file, fieldnames=["name", "home"])
#    writer.writerow({"name": name, "home": home})


import sys
import csv

def main():
    getFile()


def getFile():
    if len(sys.argv) == 3:
        fileNameIn = sys.argv[1]
        fileNameOut = sys.argv[2]
        if fileNameIn.endswith('.csv'):
            try:
                fileIn =  open(fileNameIn)


                students = []

                reader = csv.DictReader(fileIn)
                for row in reader:
                    students.append({"name": row["name"], "house": row["house"]})

                i = 0
                name = []
                nameSurnames = []
                houses = []

                while i < len(students):
                    name.append(students[i]["name"])
                    nameSplit = name[i]
                    nameSurneme = nameSplit.split(", ")
                    houses.append(students[i]["house"])
                    nameSurnames.append({"First name": nameSurneme[1], "Last name": nameSurneme[0], "House": houses[i]})
                    first = nameSurnames[i]["First name"]
                    last = nameSurnames[i]["Last name"]
                    house = nameSurnames[i]["House"]


                    i+=1
                with open(fileNameOut, 'w') as file:
                    fileOut = csv.DictWriter(file, fieldnames=["First name", "Last name", "House"])
                    fileOut.writeheader()
                    fileOut.writerow({"First name": first, "Last name":last, "House": house})


            except FileNotFoundError:
                sys.exit('File does not exist')
        else:
            sys.exit('Not a CSV file')

    elif len(sys.argv) > 2:
        sys.exit('too many arguments')
    else:
        sys.exit('too few arguments')


main()

