# set(lista) - tworzy zbiór z listy, usuwając duplikaty
nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
unique_nums = set(nums)
print(unique_nums)  # {1, 2, 3, 4, 5}

# set - zbiór, nieuporządkowany, niezmienny, nieindeksowany, unikalny
my_set = {1, 2, 3, 4, 5}
print(my_set)  # {1, 2, 3, 4, 5}

# s.add - dodaje element do zbioru
my_set.add(6)
print(my_set)  # {1, 2, 3, 4, 5, 6}

# s.remove - usuwa element ze zbioru, jeśli element nie istnieje, to błąd
my_set.remove(3)
print(my_set)  # {1, 2, 4, 5, 6}

# s.union - zwraca nowy zbiór, który jest sumą dwóch zbiorów
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print(union_set)  # {1, 2, 3, 4, 5}

# s.intersection - zwraca nowy zbiór, który jest częścią wspólną dwóch zbiorów
intersection_set = set1.intersection(set2)
print(intersection_set)  # {3}

# s.difference - zwraca nowy zbiór, który jest różnicą dwóch zbiorów
difference_set = set1.difference(set2)
print(difference_set)  # {1, 2}
