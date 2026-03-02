def main():
    x, y = get_franction()
    change_value(x, y)

def get_franction():
    try:
        x, y = input("Fraction: ").split("/")
        x = int(x)
        y = int(y)
        if y == 0 or y < x:
            print("Change y value")
            y = input("Give new y: ")
            y = int(y)
        else:
            y = int(y)
    except ValueError:
            x, y = input("Fraction: ").split("/")
            x = int(x)
            y = int(y)
    else:
        return x, y

def change_value(n, m):
    try:
        perc = round((n/m)*100)
        value = "{0}%"
        if perc >= 99:
            print('F')
        elif perc <= 1:
            print('E')
        else:
            print(value.format(perc))
    except ZeroDivisionError:
        pass
    else:
        return perc
main()
