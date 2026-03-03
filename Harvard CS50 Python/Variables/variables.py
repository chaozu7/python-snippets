"""about strings and their methods"""

# remove whitespace from str
surname = input("What is your surname? ")
surname = surname.strip()

gender = input("Are you a women? ")
# Capitalize user's name - capitalize only first word
surname = surname.capitalize()

# Capitalize every word
surname = surname.title()

print(f"My name is {surname}")

# functions chain
gender = gender.strip().title()

print(f"{gender} it's my gender.")

# split string
doublename = input("Put double name: ")
doublename = doublename.split()
print(doublename)  # ['Czarno', 'Biały']

""" intiger int """
""" float """
