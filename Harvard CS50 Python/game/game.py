import random
import sys

def main():
    n_number_int = get_n()
    x = random_n(n_number_int)
    guess(x)

def get_n():

    n_number = input("Please input n: ")

    if n_number.isdigit():
        n_number_int = int(n_number)
    else:
        n_number = input("Please input n: ")
        if n_number.isdigit():
            n_number_int = int(n_number)

    if n_number_int < 0:
        n_number = input("Please input n: ")
        if n_number.isdigit():
            n_number_int = int(n_number)
        else:
            n_number = input("Please input n: ")
            if n_number.isdigit():
                n_number_int = int(n_number)


    print(n_number_int)
    return n_number_int

def random_n(choosen):
     x = random.randint(0,choosen)
     print(x)
     return x

def guess(value):
    your_guess = input("Guess the number: ")

    if your_guess.isdigit():
        your_guess_int = int(your_guess)
    else:
        your_guess = input("Guess the number: ")
        if your_guess.isdigit():
            your_guess_int = int(your_guess)

    if your_guess_int < 0:
        your_guess = input("Guess the number: ")
        if your_guess.isdigit():
            your_guess_int = int(your_guess)
        else:
            your_guess = input("Guess the number: ")
            if your_guess.isdigit():
                your_guess_int = int(your_guess)

    while your_guess_int != value:


        if your_guess_int < value:
            print("Too small!")

        elif your_guess_int > value:
            print("Too large!")

        your_guess = input("Guess the number: ")
        if your_guess.isdigit():
            your_guess_int = int(your_guess)
        else:
            your_guess = input("Guess the number: ")
            if your_guess.isdigit():
                your_guess_int = int(your_guess)



    else:
        sys.exit("Just right!")





if __name__ == "__main__":
    main()



