import random


def main():
    level_int = get_level()
    generate_integer(level_int)




def get_level():
    level = input("Input 1,2 or 3: ")
    if level.isdigit():
        level_int = int(level)
    else:
        level = input("Input 1,2 or 3: ")

    if level_int != 1 and level_int !=2 and level_int !=3:
        level = input("Input 1,2 or 3: ")
        level_int = int(level)

    return level_int

def generate_integer(level):
    i = 10
    j = 2
    score = 0
    try:
        while i > 0:
            if level == 1:
                x = random.randint(0,9)
                y = random.randint(0,9)
            elif level == 2:
                x = random.randint(10,99)
                y = random.randint(10,99)
            elif level == 3:
                x = random.randint(100,999)
                y = random.randint(100,999)

            sum = x + y
            print(i, x, '+', y, '= ', end='')
            sum_user = int(input())
            sum_user == int(sum_user)
            if sum == sum_user:
                i-=1
                score +=1
            else:

                while j > 0 and sum != sum_user:
                    print('EEE')
                    print(x, '+', y, '= ', end='')
                    sum_user = int(input())
                    j-=1
                    
                if j == 0:
                    print(sum)
                    i-=1



            j = 2
    except ValueError:
        raise




    print("Score: ", score)

if __name__ == "__main__":
    main()
