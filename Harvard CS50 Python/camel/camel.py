var_name = input("Name of a variable: ")

for letter in var_name:
    if letter.isupper():
        var_name = var_name.replace(letter, "_" + letter)

snake_name = var_name.lower()

#snake_name = ' '

#for char in range(len(lower_name)):
#    if lower_name[char] == ' ':
#        snake_name = snake_name + '_'
#    else:
#        snake_name = snake_name + lower_name[char]

print("Snake name: ", snake_name)






