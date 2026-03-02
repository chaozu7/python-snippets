# print items as a list, prefixing by number of items,
# dict indexing

#done: prompt items, one per line, until ctrl+ d, case unsensitively, uppercase, sorted alphabetically,
def main():
    getTheList()

def getTheList():
   
    itemList = []
    shopList = {}
    index = 1
    while True:
        try:
            items = input()
            items = items.upper()
            itemList.append(items)
            itemList.sort()
        except EOFError:
            break

    for item in itemList:
        index = itemList.count(item)
        temp = dict({item: index})
        shopList.update(temp)
        index = 1

    for number, name in shopList.items():
        print(name, number)

main()
