x,y,z = input("Expression: ").split(" ")

x = int(x)
z = int(z)


if y == '+' or y == '-' or y == '*' or y ==  '/':
    if y == '+':
        wynik = x + z
        wynik = float(wynik)
        print("%.1f" % wynik)
    elif y == '-':
        wynik = x - z
        wynik = float(wynik)
        print("%.1f" % wynik)
    elif y == '*':
        wynik = x*z
        wynik = float(wynik)
        print("%.1f" % wynik)
    elif y == '/' and z !=0:
        wynik = x/z
        wynik = float(wynik)
        print("%.1f" % wynik)
else:
    print("You can't use this symbol")



