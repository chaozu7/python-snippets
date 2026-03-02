def iterPower(base, exp):
    value = 1
    
    
    if exp == 0:
        value = 1
    elif exp == 1:
        value = base
    else:
        while exp > 0:
            value = value * base
            exp -=1
       
        
    return value 
        
iterPower(10, 3)