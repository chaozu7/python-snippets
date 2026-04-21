# s.strip() - usuwa białe znaki z początku i końca stringa

s = "   Hello World!   "
print(s.strip())  # "Hello World!"

# s.lstrip() - usuwa białe znaki z początku stringa
print(s.lstrip())  # "Hello World!   "

# s.rstrip() - usuwa białe znaki z końca stringa
print(s.rstrip())  # "   Hello World!"

# s.split() - dzieli string na listę słów
print(s.split())  # ['Hello', 'World!']

s.split(",")  # dzieli string na listę słów, ale tym razem po przecinku
print(s.split(","))  # ['   Hello World!   ']

print(list("Python"))  # ['P', 'y', 't', 'h', 'o', 'n']

s.join(["Hello", "World!"])  # łączy listę słów w string, używając s jako separatora
print(s.join(["Hello", "World!"]))  # "   Hello World!   Hello   World!   "

word = ["Ala", "ma", "kota"]
print("-".join(word))  # "Ala-ma-kota"

# s.replace(old, new) - zamienia wszystkie wystąpienia old na new w stringu s
s = "Hello World!"
print(s.replace("o", "0"))  # "Hell0 W0rld!"
print(s.replace("l", "1", 1))  # "He1lo World!"

# s.find(sub) - zwraca indeks pierwszego wystąpienia sub w stringu s, lub -1 jeśli sub nie występuje
s = "Hello World!"
print(s.find("o"))  # 4
print(s.find("x"))  # -1

# s.index(sub) - zwraca indeks pierwszego wystąpienia sub w stringu s, lub rzuca ValueError jeśli sub nie występuje
s = "Hello World!"
print(s.index("o"))  # 4
try:
    print(s.index("x"))  # ValueError
except ValueError:
    print("Nie znaleziono 'x' w stringu")

# s.count(sub) - zwraca liczbę wystąpień sub w stringu s
s = "Hello World!"
print(s.count("o"))  # 2
print(s.count("x"))  # 0

# s.startswith(prefix) - zwraca True jeśli string s zaczyna się od prefix, False w przeciwnym razie
s = "Hello World!"
print(s.startswith("Hello"))  # True
print(s.startswith("World"))  # False

# s.endswith(suffix) - zwraca True jeśli string s kończy się na suffix, False w przeciwnym razie
s = "Hello World!"
print(s.endswith("!"))  # True
print(s.endswith("World"))  # False

# s.lower() - zwraca nowy string z wszystkimi literami zamienionymi na małe
s = "Hello World!"
print(s.lower())  # "hello world!"

# s.upper() - zwraca nowy string z wszystkimi literami zamienionymi na wielkie
s = "Hello World!"
print(s.upper())  # "HELLO WORLD!"

# isalpha() - zwraca True jeśli wszystkie znaki w stringu są literami, False w przeciwnym razie
s = "Hello"
print(s.isalpha())  # True
s = "Hello123"
print(s.isalpha())  # False

# isdigit() - zwraca True jeśli wszystkie znaki w stringu są cyframi, False w przeciwnym razie
s = "12345"
print(s.isdigit())  # True
s = "12345a"
print(s.isdigit())  # False

# ord() - zwraca kod ASCII znaku
print(ord("A"))  # 65
print(ord("a"))  # 97

# chr() - zwraca znak odpowiadający kodowi ASCII
print(chr(65))  # 'A'
print(chr(97))  # 'a'

# sub in s
s = "Hello World!"
print("Hello" in s)  # True
print("Python" in s)  # False
