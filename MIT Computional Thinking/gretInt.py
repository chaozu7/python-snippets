def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    max_a = []
    max_b = []
    if a > b:
        var_max = b
        if a%var_max == 0:
            var_max = b
        else:
            while a%var_max != 0:
                var_max -= 1
            print(var_max)
        if b%var_max == 0:
            var_max = var_max
            print(var_max)
        else:
            while b%var_max != 0:
                var_max -= 1
            print(var_max)
        print(var_max)
    elif b > a:
        var_max = a
        if b%var_max == 0:
            var_max = a
        else:
            while b%var_max != 0:
                var_max -= 1
        if a%var_max == 0:
            var_max = var_max
        else:
            while a%var_max != 0:
                var_max -= 1
        print(var_max)
        
        
        
    
    
    
gcdIter(304,272)



def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x

print(gcd(30,15))
        
