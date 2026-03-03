def main():
    x = int(input("Give me a number: "))
    if is_even(x):
        print("Number is even")
    else:
        print("Number is odd")


def is_even(n):
  # return True if n % 2 == 0 else False
    return n % 2 == 0


main()
