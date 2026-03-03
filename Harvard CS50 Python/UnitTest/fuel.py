def main():
    fraction = input("Fraction: ")
    converted_f = convert(fraction)
    gauge(converted_f)

def convert(fraction):
    try:
        x,y = fraction.split("/")
        x = int(x)
        y = int(y)
        perc = x/y
        if perc <= 1:
            converted_f = round((x/y)*100)
            return converted_f
        else:
            fraction = input("Fraction: ")
            pass
    except (ValueError, ZeroDivisionError):
            raise

def gauge(percentage):
    try:
        value = "{0}%"
        if percentage >= 99:
            print('F')
        elif percentage <= 1:
            print('E')
        else:
            output = print(value.format(percentage))
    except ZeroDivisionError:
        pass
    else:
        return output
main()
