#zmienne
c = 300000000
#zapytanie do uzytkownika o podanie masy, zapisujemy ją w zmiennej m
m = input("Podaj masę: ")
#zmieniamy m na int - to się nazywa konwersja, jeśli podany został ciąg liter program wyrzuci błąd
m = int(m)
#sprawdzamy czy m jest większe od zera, jeśli nie prosimy uzytkownika o powtórkę
if m < 0:
    m = input("Podaj masę więszą od zera: ")
#wzór - to nic innego jak przypisanie wartości do zmiennej E
E = m * c**2
#wyświetlamy informację dla użytkownika o wyniku - dodaję tekst i oddzielam przecinkiem od wartości zmiennej E
print("Warość energii jest równa", int(E))