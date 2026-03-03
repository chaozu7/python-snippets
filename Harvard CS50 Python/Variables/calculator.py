

#x = int(input("Give me x: "))
#y = int(input("Give me y: "))

x = float(input("Give me x: "))
y = float(input("Give me y: "))


print(y + x)

# round the results

k = y - x

print(round(y - x))

# format big numbers - separate by , ex 1,000,000
print(f"{k:,}")


j = round(x/y, 2)
print(j)


def square(j, k):
    return j + k


square(j, k)
