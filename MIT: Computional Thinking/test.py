
secretWord = 'audi'

lettersGuessed = 'aui'

    

partialWord = ''
 

for letter in secretWord:
   if letter in lettersGuessed:
       partialWord += letter
   else:
       partialWord += '_ '
print(partialWord)
   
    

    