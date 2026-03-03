
# definiuję zmienną licznika
index = 0 

# definiuję listę, do które będę zapisywał liczby
numbers = []

# używam pętli 'while' czyli 'póki dany warunek jest spełniony'
# póki index jest mniejszy od 10
while index < 10:
    # używam try - czyli spróbuj, robię to po to żeby sprawdzić czy użytkownik podaje liczbę
    try:
        #do zmiennej number wprowadzam wartość od użytkownika, od razu zmieniam ją z string na int, liczyli liczba
        number = int(input("Podaj liczbę "))
        #dodaję poprawną wartość do mojej listy numbers, dodaję na koniec
        numbers.append(number)
        #powiększam wartość index, po to żeby po wpisaniu 10 liczb pęta się zakończyła
        index +=1
    # jeśli uzytkownik wpisze coś czego nie da się zamienić na liczbę to wypisuję komunikat i nie powiększam indeksu
    except ValueError:
        print("Podaj liczbę.")

# wypisuję wartości na ekran, * znaczy tyle że usuwam []  z listy żeby nie wyglądała tak: [1,2,3,4], usuwa mi to też przecinki, więc ponownie je dodaje jako: sep to separator, tu ustawiam przecinek, end to koniec linii - chcę żeby kropka była w tej samej linii więc to tutaj zaznaczam jako brak końca linii
print(*numbers, sep=", ", end="")
print(".")
