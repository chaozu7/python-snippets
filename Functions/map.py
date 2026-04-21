print(list(map(int, ["1", "2", "3"])))  # [1, 2, 3]
print(list(map(str, [1, 2, 3])))  # ['1', '2', '3']
print(list(map(lambda x: x**2, [1, 2, 3])))  # [1, 4, 9]
print(list(map(str.upper, ["hello", "world"])))  # ['HELLO', 'WORLD']


# lambda - funkcja anonimowa, która może mieć dowolną liczbę argumentów, ale tylko jedno wyrażenie
# map - funkcja, która stosuje funkcję do każdego elementu iterowalnego i zwraca map object, który jest iterowalny

print(list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5])))  # [2, 4]
# filter - funkcja, która filtruje elementy iterowalnego za pomocą funkcji, która zwraca True lub False, i zwraca filter object, który jest iterowalny

# sorted(list, key=function) - sortuje listę za pomocą funkcji, która zwraca wartość, która jest używana do sortowania
print(sorted(["apple", "banana", "cherry"], key=len))  # ['apple', 'cherry', 'banana']
