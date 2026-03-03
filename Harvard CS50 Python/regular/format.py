import re


name = input("What's your name? ").strip()

#
#if "," in name:
##    last, first = name.split(", ")
#    name = f"{first}{last}"

#print(f"hello, {name}")
if matches := re.search(r"^(.+), *(.+)$", name):
    name = matches.groups(2) + " " + matches.group(1)
    

print(f"hello, {name}")