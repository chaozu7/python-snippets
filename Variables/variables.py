"""about strings and their methods"""

"""# remove whitespace from str
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
"""
""" intiger int """
""" float """

# List#

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

print(months[-1])  # December
print(max(months))  # September
print(sorted(months))
print(min(months))  # April
print(" and ".join(["March", "April"]))

bestMonths = []
bestMonths.append("April")
print(bestMonths)
# tuples
dimensions = 52, 40, 100
length, width, height = dimensions
print("The dimensions are {} x {} x {}".format(length, width, height))

# set
numbers = [1, 2, 6, 3, 1, 1, 6]
unique_nums = set(numbers)
print(unique_nums)

unique_nums.add(7)
print(unique_nums)
unique_nums.pop()
print(unique_nums)

# dictionary
elements = {"hydrogen": 1, "helium": 2, "carbon": 6}
print(elements["helium"])  # print the value mapped to "helium"
elements["lithium"] = 3  # insert "lithium" with a value of 3 into the dictionary
print("carbon" in elements)
print(elements.get("dilithium"))
