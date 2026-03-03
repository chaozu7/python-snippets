

#prompt for item until ctrl+d, case insensitively, ignor input that is not an item, .title()
# $total item, two decimal places

def main():

    item = get_order("Item: ")

def get_order(prompt):
    class Counter(dict):
        def __missing__(self, key):
            return 0

    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    total = 0

    d = Counter(menu)

    while d != 0:
        try:
            item = input(prompt)
            item = item.title()
            if item in menu:
                total = total + menu.get(item)
                print("Total: $", ("%.2f" % total), sep="")
        except EOFError:
            return 0




main()
