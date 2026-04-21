# listy są mutable - można je modyfikować


# max
nums = [3, 1, 4, 1, 5, 9]
print(max(nums))  # 9

# min
print(min(nums))  # 1

# len
print(len(nums))  # 6

# sum
print(sum(nums))  # 23

# sorted
print(sorted(nums))  # [1, 1, 3, 4, 5, 9]
print(sorted(nums, reverse=True))  # [9, 5, 4, 3, 1, 1]

# sort - ona zapisuje się jako posortowana
nums.sort()
print(nums)  # [1, 1, 3, 4, 5, 9]
nums.sort(reverse=True)
print(nums)  # [9, 5, 4, 3, 1, 1]

# append - dodaje element na koniec listy
nums.append(2)
print(nums)  # [9, 5, 4, 3, 1, 1, 2]

# extend - dodaje elementy z innej listy na koniec listy
nums.extend([6, 5])
print(nums)  # [9, 5, 4, 3, 1, 1, 2, 6, 5]

# insert - dodaje element na podany indeks
nums.insert(0, 10)
print(nums)  # [10, 9, 5, 4, 3, 1, 1, 2, 6, 5]

# inser - dodaje element na podany indeks
nums.insert(2, 33)
print(nums)  # [10, 9, 33, 5, 4, 3, 1, 1, 2, 6, 5]

# remove - usuwa pierwsze wystąpienie elementu z listy
nums.remove(1)
print(nums)  # [10, 9, 33, 5, 4, 3, 1, 2, 6, 5]

# pop - usuwa element z listy i zwraca go
removed = nums.pop(2)
print(removed)  # 33
print(nums)  # [10, 9, 5, 4, 3, 1, 2, 6, 5]

# pop(3) - usuwa element z listy i zwraca go
removed = nums.pop(3)
print(removed)  # 4
print(nums)  # [10, 9, 5, 3, 1, 2, 6, 5]

# clear - usuwa wszystkie elementy z listy
nums.clear()
print(nums)  # []

# count - zwraca liczbę wystąpień elementu w liście
nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
print(nums.count(1))  # 2
print(nums.count(6))  # 0

# index - zwraca indeks pierwszego wystąpienia elementu w liście
print(nums.index(3))  # 2
try:
    print(nums.index(6))  # ValueError
except ValueError:
    print("Nie znaleziono 6 w liście")

# usuwanie duplikatów z listy
nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
unique_nums = list(set(nums))
print(unique_nums)  # [1, 2, 3, 4, 5]

# zip - łączy dwie listy w jedną listę krotek
list1 = [1, 2, 3]
list2 = ["a", "b", "c"]
zipped = zip(list1, list2)
print(list(zipped))  # [(1, 'a'), (2, 'b'), (3, 'c')]

for num, letter in zip(list1, list2):
    print(f"{num} - {letter}")  # 1 - a 2 - b 3 - c

# enumerate - zwraca indeks i wartość elementu w liście
nums = [10, 20, 30]
for index, num in enumerate(nums):
    print(f"{index} - {num}")  # 0 - 10 1 - 20 2 - 30
