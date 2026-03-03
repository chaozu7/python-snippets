from datetime import date
import sys
import inflect
import operator

format = inflect.engine()

def main():
    today = date.today()
    try:
        birth = input("What is your date of birtch? ")
        difference = operator.sub(today, date.fromisoformat(birth))
     #   print(difference)
        print(convert(difference.days))
    except ValueError:
        sys.exit("Invalid date")

def convert(time):
    minutes = time * 24 * 60
    return f"{(format.number_to_words(minutes, andword='')).capitalize()} minutes"




if __name__ == "__main__":
    main()
