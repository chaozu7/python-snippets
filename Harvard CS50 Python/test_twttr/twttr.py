# (A, E, I, O, and U)
def main():
    input_twiit = input("Insert: ")
    print(shorten(input_twiit))



def shorten(input_twiit):
    vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'O', 'o', 'U', 'u']
    for char in input_twiit:
        if char in vowels:
            input_twiit = input_twiit.replace(char, "")
    return input_twiit

if __name__ == "__main__":
    main()


