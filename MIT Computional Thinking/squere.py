def prosiaczek(x):
    x = (x**2)
    
    return x
    
    
print(prosiaczek(2))


def przemek(x):
    
    x = prosiaczek(x)**2
    
    return x
    
print(przemek(3))

def odd(x):
    
    return x%2 == 0 

print(odd(2))

