def main():
    print_column(3)
    print("\n")
    print_row(4)
    print("\n")
    print_square(3)


def print_column(height):
    for _ in range(height):
        print("#")


def print_row(width):
    print("?" * width)


def print_square(size):
    for i in range(size):
        for j in range(size):
            print("#", end="")
        # only after row
        print()


# def print_square(size):
#    for i in range(size):
#       print("#")

main()
