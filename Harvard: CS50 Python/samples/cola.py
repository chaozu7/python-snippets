#zmienne
cost = 50
insert_coins = 0
#wrzucamy monety dopóki licznik nie dojdzie do 0
while cost <= 50 and cost > 0:
    insert_coins = input("Wrzuć monetę: ")
    insert_coins = int(insert_coins)
#wrzucamy 5, 10, 20 groszy. Jak wiemy w pOlsce nie ma 25 groszówek
#abs() żeby nie było -
    if insert_coins == 5 or insert_coins == 10 or insert_coins == 20:
            cost = cost - insert_coins
            if cost > 0:
                print("Dopłać:", cost)
            elif cost == 0:
                print("Reszta:", abs(cost))
                print("Trzymaj swoją Colę!")
            elif (cost - insert_coins < 0):
                 print("Reszta:", abs(cost))
                 print("Trzymaj swoją Colę!")
    else:
        cost = cost
        print("Nie przyjmuję takich monet!")
        print("Dopłać:", cost)