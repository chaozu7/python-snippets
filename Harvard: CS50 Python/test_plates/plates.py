def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    char_limit(s)
    char_only(s)
    is_lower(s)
    letter_first(s)
    num_valid(s)
    first_number(s)
    if char_limit(s) and char_only(s) and is_lower(s) and letter_first(s) and num_valid(s) and first_number(s):
        return True

# no uppercases
def is_lower(s):
    if s.islower():
        return False
    else:
        return True

# max 6 min 2 char
def char_limit(s):
    if len(s) <=6 and len(s) >= 2:
        return True
    else:
        return False

# only letters and numbers
def char_only(s):
    status = 1
    for char in s:
        if char.isnumeric() or char.isalpha():
            status = 1
        else:
            status = 0
            if status == 0:
                return False
    if status == 1:
        return True


# at last 2 letters
def letter_first(s):
    index = 2
    i = 1
    counter = 0
    for char in s:
        while index >= i:
            if char.isalpha():
                i +=1
                return True
            else:
                i +=1
                counter +=1
                return False
    if counter > 0:
        return False

# number at the end
def num_valid(s):
    stat = 0
    is_ok = True
    for char in s:
        if char.isnumeric():
            stat += 1
        if stat > 0 and char.isalpha():
            return False
        elif stat > 0 and char.isnumeric():
            is_ok = True
    if stat == 0 or is_ok == True:
        return True


# first number couldnt be 0

def first_number(s):
    counter = 0
    for char in s:
        if char.isnumeric():
            counter += 1
            if char == '0' and counter == 1:
                return False
            elif char !='0' and counter == 1:
                return True
    if counter == 0:
        return True

if __name__ == "__main__":
    main()
