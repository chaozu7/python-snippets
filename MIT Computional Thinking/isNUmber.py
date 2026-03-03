secret_number = 8
 
def isMyNumber(x):
   
    if x == secret_number:
       
        return 0
    elif x > secret_number:
        
        return 1
    elif x < secret_number:
       
        return -1
    
isMyNumber(2)

def jumpAndBackpedal(isMyNumber):
    '''
    isMyNumber: Procedure that hides a secret number. 
     It takes as a parameter one number and returns:
     *  -1 if the number is less than the secret number
     *  0 if the number is equal to the secret number
     *  1 if the number is greater than the secret number
 
    returns: integer, the secret number
    ''' 
    guess = 1

    
    if isMyNumber(guess) == 0:
   
        return guess
    
    while isMyNumber(guess) != 0:
        if isMyNumber(guess) == 1:
            guess -= 1
        elif isMyNumber(guess) == -1:
            guess += 1
        
    print(guess)
    return guess

jumpAndBackpedal(isMyNumber)

