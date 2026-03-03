#import - w ten sposób podłączamy się do biblioteki już napisanych funkcji w Pythonie - inni programiści się napocili, my korzystamy
#cowsay - biblioteka odpowiedzialna za to, że system wyświetla zwierzątka
import cowsay
#sys - biblioteka odpowiedzialna za to, że po nazwie pliku możemy od razu dodawać wartości, bez pytania użytkownika, wygląda to tak:
#python pip.py argument - jeśli chcemy dinozaura
#python pip.py argument argument - jeśli chcemy 
import sys
# len() to wbudowana funkcja, która przelicza - tutaj przelicza ilość argumentów
# program numeruje elementy listy od zera czyli 0 jest pierwszym elementem
if len(sys.argv) == 2:
    cowsay.cow("test1" + sys.argv[1])
    
elif len(sys.argv) == 3:
    cowsay.milk("test2" + sys.argv[1] + " " + sys.argv[2])

elif len(sys.argv) == 4:
    cowsay.cheese("test3" + sys.argv[1] + " " + sys.argv[2] + " " + sys.argv[3])

else:
    cowsay.trex("Nie wiem o co ci chodzi? ")