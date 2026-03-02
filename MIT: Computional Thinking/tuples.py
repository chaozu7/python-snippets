


def odd(testTouple):
    finalTouple = []


    i = 1

    for i in range(len(testTouple)):
        if i%2 == 0:
            y = testTouple[i]
            finalTouple.append(y)
        
        i +=1
    
    finalTouple = tuple(finalTouple)            
    return finalTouple

k = odd((1,2,3,'k', True, 9))
print(k)

        