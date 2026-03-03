import math

print('Please think of a number between 0 and 100!')

number_max = 100
number_min = 0


guess = int(math.floor((number_max+number_min)/2))

print("Is your number", guess, "?")

answer = ''

while answer != 'c':
    answer = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if answer == 'h':
        number_max = guess
        guess = int(math.floor((number_max+number_min)/2))
        print("Is your number", guess, "?")
    elif answer == 'l':    
        number_min = guess
        guess = int(math.floor((number_max+number_min)/2))
        print("Is your number", guess, "?")
        
    elif answer == 'c':
        print("Game over. Your secret number was:", int(guess))
    
    else:
        print("Sorry, I did not understand your input.")
        print("Is your number", guess, "?")
        