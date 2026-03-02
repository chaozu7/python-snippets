amount_due = 50
insert_coins = 0

while amount_due <= 50 and amount_due > 0:
    insert_coins = input("Insert Coin: ")
    insert_coins = int(insert_coins)

    if insert_coins == 5 or insert_coins == 10 or insert_coins == 25:
            amount_due = amount_due - insert_coins
            if amount_due > 0:
                print("Amount Due:", amount_due)
            if amount_due == 0:
                print("Change Owed:", abs(amount_due))
                print("Here is your coke budy!")
                break
            if (amount_due - insert_coins < 0):
                 print("Change Owed:", abs(amount_due))
                 print("Here is your coke budy!")
    else:
        amount_due = amount_due
        print("Wrong coin, bam")
        print("Amount Due:", amount_due)




