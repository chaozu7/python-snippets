
s = 'cigeccgueykuiuqxihcsw'

vowels = ['a', 'e', 'i', 'o', 'u']
i = 0


for vowel in vowels:
    i += s.count(vowel)
    
i = str(i)    

info = "Numver of vowels: " + i 

print(info)