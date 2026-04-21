import math


print(math.sqrt(16))  # zawsze float
print(math.sqrt(0))

# dla ujemnej błąd

# w górę
print(math.cell(4.2))  # 5
print(math.cell(-4.2))  # 4

# w dół

print(math.floor(9.1))

# NWD - największy wspólny dzielnik

print(math.gcd(12, 15))  # 3
print(math.gcd(100, 75))  # 25

# NWW - najmniejsza wspólna wielokrotność

print(math.lcm(12, 15))  # 60
print(math.lcm(100, 75))  # 300
