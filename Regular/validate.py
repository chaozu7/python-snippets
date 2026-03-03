email = input("What's your email? ").strip()

# poor
# if "@" in email and ".":
#
# print("Valid")else:
#    print("Invalid")

username, domain = email.split("@")

if domain.endswith(".edu"):
    print("Valid")
else:
    print("Invalid")


# re - library for regular expressions
