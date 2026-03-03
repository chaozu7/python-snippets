#write to file:

#name = input("What is your name? ")

#file = open("names.txt", "w")
#with open("names.txt", "a") as file:
#    file.write(f"{name}\n")


# read
# unsorted
with open("names.txt", "r") as file:
    for line in file:
        print("hello,", line.rstrip())
    
#print always add a new line to the code


# read 
# sorted

### longer

print ("\nLonger way")

names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())
        
for name in sorted(names):
    print(f"hello, {name}")

### shorter

print ("\nShorter way")

with open("names.txt") as file:
    for line in sorted(names, reverse=True):
        print("hello,", line.rstrip())