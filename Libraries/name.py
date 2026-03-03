import sys


# Check for errors
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments, use quotes")

# Print the name
print("hello, my name is", sys.argv[1])
