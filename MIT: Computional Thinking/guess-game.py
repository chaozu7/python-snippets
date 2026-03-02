def lessThan4(aList):
    subList = []
    for elem in aList:
        if len(elem) < 4:
            subList.append(elem)
    return subList
    
a = ["apple", "cat", "dog", "banana"]   

lessThan4(a)



def keysWithValue(aDict, target):
    
   keys = [key for key, val in aDict.items() if val == target]
   return keys
    
a = {1: 2, 2:4, 3:4}    
keysWithValue(a, 1)
