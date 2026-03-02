name = input("What's your name? ")


match name:
    case "Harry" | "Ron" | "Hermione":
        print("Gryffindor")
    case "Draco":
        print("Slytherinn")
    case _:
        print("Who?")
