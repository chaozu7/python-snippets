
def main():
    greeting = input("Greet me, please ")


    print(value(greeting))

def value(greeting):
    greeting = greeting.strip().upper()
    greeting_letters = []
    greeting_first = greeting.split()
    for char in greeting:
        greeting_letters.append(char)
    # hello $0
    if greeting_first[0] == 'HELLO' or greeting_first[0] == 'HELLO,':
        return(0)
    # with 'h' $20
    elif greeting_letters[0] == 'H' and greeting_first[0] != 'HELLO' and greeting_first[0] != 'HELLO,':
        return(20)
    # otherwise $100
    else:
        return(100)



if __name__ == "__main__":
    main()
