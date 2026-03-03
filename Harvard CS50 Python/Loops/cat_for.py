# for i in [0, 1, 2]:
#    print("meow")

# we use _ name for variable because it is needed to run the loop but for us is not necessary
""" for _ in range(3):
    print("meow") """

# end=""means without extra blank line after
# print("meow\n" * 3, end="")


while True:
    n = int(input("What's n? "))
    if n > 0:
        break
for _ in range(n):
    print("meow")
