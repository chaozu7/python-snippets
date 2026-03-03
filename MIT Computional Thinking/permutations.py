def is_list_permutation(L1, L2):
    
    common = []
        
    if len(L1) != len(L2):
        return False
    elif len(L1) == 0 and len(L2) == 0:
        message = (None, None, None)
        return message
    else:
        for elm in L1:
            if elm in L2:
               
                common.append(elm)            
            else:
                return False
        howMany = []
        temp = 0
        
        for v in common:
            howMany.append(common.count(v))
            if common.count(v) >= temp:
                temp = common.count(v)
                biggestVal = v
          
        info = (biggestVal, max(howMany), type(biggestVal))
    print(info)
      
        
        
        
            
            
is_list_permutation([1, 2, 1],[2, 1, 2])  
#is_list_permutation([1,4,2,2, 20, 35, 35, 35], [1,2,2,4, 35, 35, 35, 20])
