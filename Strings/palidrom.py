import string

# get the value
string_1 = input("please insert a value ")

# clean the text
string_1 = string_1.lower()

clean_str = "".join(letter for letter in string_1 if letter not in string.punctuation)

clean_str = clean_str.replace(" ", "")

# check if palidrom
i = -1
is_palidrom = 0

for letter in range(len(string_1)):
    if string_1[letter] == string_1[i]:
        i += -1
        is_palidrom += 1
    else:
        is_palidrom = 0


if is_palidrom == len(string_1):
    print("Tak, to palidrom")
else:
    print("Nie, to nie jest palidrom")
