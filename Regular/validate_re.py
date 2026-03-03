import re

email = input("What's your email? ").strip()
# special sequence
# if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9]+\.edu$", email):
if re.search(r"^\w+@(\w+\.)?\w+\.(edu|com|pl)$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")
