from validator_collection import checkers

email = input("What is your email address? ")

if checkers.is_email(email):
    print("Valid")
else:
    print("Invalid")

