def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    
    
    while len(aStr) > 1:    
        middle = int(len(aStr)/2)
        
        if aStr.rfind(char) == middle:
            print(char)
            break
        elif aStr.rfind(char) > middle:
            aStr = aStr[middle:]
        elif aStr.rfind(char) < middle:
            aStr = aStr[:middle]        
   

isIn('l', 'aaaabcdeffffuuul')