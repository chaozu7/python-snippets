animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

print(animals.values())
print(animals.keys())


def how_many(aDict):
    valuesDict = aDict.values()  
    count = 0
    for i in valuesDict:
        count += len(i)
        
    return count
    
    
how_many(animals)


test = {'u': []}

def biggest(aDict):
   
    
    max = 0
    
    for i in aDict:
        
        valueDict = aDict[i]
        lenght = len(valueDict)
       
        temp = lenght
        if temp >= max:
            max = temp
            maxKey = i
    return maxKey
            
  
    
biggest(test)