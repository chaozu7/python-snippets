#import - w ten sposób podłączamy się do biblioteki już napisanych funkcji w Pythonie - inni programiści się napocili, my korzystamy
#cowsay - biblioteka odpowiedzialna za to, że system wyświetla zwierzątka
import cowsay
#sys - biblioteka odpowiedzialna za to, że po nazwie pliku możemy od razu dodawać wartości, bez pytania użytkownika, wygląda to tak:
#python pip.py argument - jeśli chcemy dinozaura
#python pip.py argument argument - jeśli chcemy 
import sys
# len() to wbudowana funkcja, która przelicza - tutaj przelicza ilość argumentów
if len(sys.argv) == 2:
    cowsay.cheese("Jak samopoczucie " + sys.argv[1])
    
if len(sys.argv) == 3:
    cowsay.cow("Co u Ciebie, " + sys.argv[1] + " " + sys.argv[2])
