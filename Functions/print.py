# print

# print(*objects, sep='', end='\n')

print(1, 2, 3, sep="-")  # 1-2-3
print("Hello", end="!")  # Hello! default to \n, jeśli damy samo ! nie skończy linii

for _ in range(10):
    print("Hello", end=" ")

for i in range(10):
    print(chr(65) * i)


name = "Kama"
age = 20

print(f"{name} ma {age} lat")

pi = 3.14159265

print(f"Pi zaokląglone {pi:.2f}")
