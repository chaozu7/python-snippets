import inflect

p = inflect.engine()

name = input("Name: ")
nameList = []

nameList.append(name)


while True:
    try:
        name = input("Name: ")
        nameList.append(name)

    except EOFError:
        nameList = p.join((nameList))
        adieuList = "Adieu, adieu, to "+ nameList
        print(adieuList)
        exit()



