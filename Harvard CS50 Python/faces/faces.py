
def convert():
    toEmoi = input("Give a text with :( or :) " )
    if ':)' in toEmoi:
        print(toEmoi.replace(':)','🙂'))
    if ':(' in toEmoi:
        print(toEmoi.replace(':(','🙁'))
    if ':(' in toEmoi and ':)' in toEmoi:
        toEmoi = toEmoi.replace(':)','🙂')
        toEmoi = toEmoi.replace(':(','🙁')
        print(toEmoi)

def main():
    convert()

main()

