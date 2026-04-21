from collections import Counter

slownik = {"imie": "Jan", "nazwisko": "Kowalski", "wiek": 30}

print(slownik["imie"])  # Jan
print(slownik["nazwisko"])  # Kowalski
print(slownik["wiek"])  # 30

# slownik.keys() - zwraca listę kluczy
print(slownik.keys())  # dict_keys(['imie', 'nazwisko', 'wiek'])

# slownik.values() - zwraca listę wartości
print(slownik.values())  # dict_values(['Jan', 'Kowalski', 30])

# slownik.items() - zwraca listę krotek (klucz, wartość)
print(
    slownik.items()
)  # dict_items([('imie', 'Jan'), ('nazwisko', 'Kowalski'), ('wiek', 30)])

for klucz, wartosc in slownik.items():
    print(f"{klucz}: {wartosc}")
# imie: Jan
# nazwisko: Kowalski
# wiek: 30

# slownik.get() - zwraca wartość dla podanego klucza, jeśli klucz nie istnieje, to zwraca None
print(slownik.get("imie"))  # Jan
print(slownik.get("adres"))  # None

# slownik.pop() - usuwa element z słownika i zwraca jego wartość
wiek = slownik.pop("wiek")
print(wiek)  # 30
print(slownik)  # {'imie': 'Jan', 'nazwisko': 'Kowalski'}

# slownik.update() - aktualizuje słownik o nowe klucze i wartości
slownik.update({"adres": "ul. Kwiatowa 10", "wiek": 31})
print(
    slownik
)  # {'imie': 'Jan', 'nazwisko': 'Kowalski', 'adres': 'ul. Kwiatowa 10', 'wiek': 31}

# slownik.clear() - usuwa wszystkie elementy ze słownika
slownik.clear()

print(slownik)  # {}

# dict.fromkeys - tworzy słownik z podanymi kluczami i wartością domyślną
keys = ["a", "b", "c"]
default_value = 0
new_dict = dict.fromkeys(keys, default_value)
print(new_dict)  # {'a': 0, 'b': 0, 'c': 0}

new_dict["a"] = 1
print(new_dict)  # {'a': 1, 'b': 0, '   c': 0}

# new_dict.setdefault() - zwraca wartość dla podanego klucza, jeśli klucz nie istnieje, to dodaje go do słownika z wartością domyślną i zwraca tę wartość
print(new_dict.setdefault("d", 2))  # 2
print(new_dict)  # {'a': 1, 'b': 0, 'c': 0, 'd': 2}


# Counter - zlicza wystąpienia elementów w kolekcji
from collections import Counter

lista = ["a", "b", "c", "a", "b", "a"]
counter = Counter(lista)
print(counter)  # Counter({'a': 3, 'b': 2, 'c': 1})
print(counter["a"])  # 3
print(counter["b"])  # 2
print(counter["c"])  # 1

# dict(sorted(counter.items())) - sortuje słownik według kluczy
sorted_counter = dict(sorted(counter.items(), key=lambda item: item[0]))
print(sorted_counter)  # {'a': 3, 'b': 2, 'c': 1}
