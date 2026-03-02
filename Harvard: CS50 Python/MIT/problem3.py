
s = 'vurjhzolkunye'

substring = ''
max_substring = ''
temp_max = ''
temp = s[0]

for letter in s:
    if letter < temp:
        temp_max = substring
        substring =  letter    
         
    elif letter >= temp:
        
        substring += letter
        temp_max = substring
  
    
    temp = letter
    if len(temp_max) > len(max_substring):
        max_substring = temp_max
   
        

print("Longest substring in alphabetical order is: ", max_substring)