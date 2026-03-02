greeting = input("Greet me, please ")
greeting = greeting.strip().upper()
greeting_letters = []
greeting_first = greeting.split()

for char in greeting:
    greeting_letters.append(char)

if len(greeting) > 1:
    # hello $0
    if greeting_first[0] == "HELLO" and len(greeting_first) == 1:
        print("$0")
    # with 'h' $20
    elif greeting_letters[0] == "H":
        print("$20")
    # otherwise $100
    else:
        print("$100")
else:
    print("string is too short")
