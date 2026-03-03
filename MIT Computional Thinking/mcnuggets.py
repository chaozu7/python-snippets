import random

def McNuggets(n):
    
    #6a+9b+20c = n
    
    
    if n%20 == 0 or n%9 == 0 or n%6 == 0:
        print(True)
    elif n < 6:
        print(False)
        
    max_a = n // 6 + 1
    max_b = n // 9 + 1
    max_c = n // 20 + 1
    
    for c in range(max_c):
        for b in range(max_b):
            for a in range(max_a):
                if (6*a + 9*b + 20*c) == n:
                    return True
                if (6*a + 9*b + 20*c) > n:
                    break
            if (9*b + 20 *c) > n:
                break
        if (20*c) > n:
            break
        
    return False
    
    
   
     
    '''
    howMany = 0
    value = 6*a + 9*b + 20*c
    
    print(a,b,c)
    print("value 1:", value)
    
    if n == value:
        return True
    
    if n > value:
        howMany = n - value
        print("how many 1", howMany)
        if howMany%6 == 0 or howMany%9 == 0 or howMany%20 == 0:
            print('jupi')
        else:
            if howMany >= 44:
                while howMany >= 44:
                    howMany -= 20
            if howMany < 44:
                while howMany >=9:
                    howMany -=9 
            if howMany < 9:
                while howMany < 9 and howMany >= 6:
                    howMany -=6
            
            print(howMany)
            
               
       
    elif n < value:
        howMany = value - n
        print("how many 1:", howMany)
        if howMany%6 == 0 or howMany%9 == 0 or howMany%20 == 0:
            print('jupi')
        else:
            if howMany >= 44:
                while howMany >= 44:
                    howMany -= 20
            if howMany < 44:
                while howMany >=9:
                    howMany -=9 
            if howMany < 9:
                while howMany < 9 and howMany >= 6:
                    howMany -=6
            
            
            
            print(howMany)

        
    
    
    # 6 12 18 24
    # 9 18 27
    # 20
    
    
  
    
    
    
    '''
    
                
McNuggets(45)

    