# wartość bezwzględna

print(abs(-19))  # 19
print(abs(3.5))  # 3.5
print(abs(0))  # 0


# potęgowanie
print(pow(2, 3))
print(pow(9, 0.5))  # pierwiastek
print(9**1)


# iloraz + reszta

q, r = divmod(10, 3)

print(f"{q} to wynik dzielenia a {r} to reszta")

# round

print(round(3.14159, 2))
print(round(3.14159, 0))
print(round(3.14159, 3))

# binarne

print(bin(10))
print(bin(10)[2:])

# szesnastkowe

print(hex(255))
print(hex(25125)[2:])

# z podanego systemu na 10
print(int("1010", 2))
print(int("FF", 16))

# format
print(format(5, "08b"))  # 2
print(format(5, "08x"))  # 8
print(format(5, "08o"))  # 16
