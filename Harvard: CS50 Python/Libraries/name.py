import sys


# Check for errors
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
# kamila - kamila
#"kamila anna" - kamila anna

# Print the name

for arg in sys.argv[1:]:
    print("hello, my name is", arg)
