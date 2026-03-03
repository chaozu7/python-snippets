import sys
from PIL import Image
from PIL import ImageOps
import os

def main():
    getFile()


def getFile():
    if len(sys.argv) == 3:
        fileNameIn = sys.argv[1]
        fileNameOut = sys.argv[2]
        fileNameIn = fileNameIn.lower()
        fileNameOut = fileNameOut.lower()
        shirt = Image.open('shirt.png')

        if fileNameIn.endswith('.png') or fileNameIn.endswith('.jpg') or fileNameIn.endswith('.jpeg') or fileNameOut.endswith('.png') or fileNameOut.endswith('.jpg') or fileNameOut.endswith('.jpeg'):
            try:
                person_ext = os.path.splitext(fileNameIn)
                shirt_ext = os.path.splitext(fileNameOut)

                if person_ext[1] != shirt_ext[1]:
                    sys.exit('Wrong type')

                else:
                    person = Image.open(fileNameIn)
                    person_size = person.size
                    shirt_size = shirt.size
                    person = ImageOps.fit(person, shirt_size)
                    person.paste(shirt, box = (0, 0), mask = shirt)
                    person.save(fileNameOut, format=None)



            except FileNotFoundError:
                sys.exit('File does not exist')
        else:
            sys.exit('Invalid input')

    elif len(sys.argv) > 2:
        sys.exit('too many arguments')
    else:
        sys.exit('too few arguments')


if __name__ == "__main__":
    main()

