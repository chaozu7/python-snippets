# prompt for a date in month-day-year x/y/zzzz or April 7, 1990
# output in YYYY-MM-DD
#validate the number of a days
# print(f"{n:02}")
def main():

    date = getDate("Date: ")

def getDate(prompt):

    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"]

    stat = 0

    try:
        while stat !=1:
            date = input(prompt)
            if '/' in date:
                date_to_check = date.split('/')
                if int(date_to_check[0]) <= 12:
                    month = date_to_check[0].strip()
                else:
                    stat = 0
                    continue
                if int(date_to_check[1]) <= 31:
                    day = date_to_check[1].strip()
                else:
                    stat = 0
                    continue

            elif ',' in date:
                date_to_check = date.replace(',', '')
                date_to_check = date_to_check.split(' ')
                if date_to_check[0] in months:
                    month_index = months.index(date_to_check[0])
                    month = str(month_index + 1)
                else:
                    stat = 0
                    continue
                if int(date_to_check[1]) <= 31:
                    day = date_to_check[1].strip()
                else:
                    stat = 0
                    continue
            else:
                stat = 0
                continue

            year = date_to_check[2].strip()
            print(year + '-' + f"{int(month):02}" + '-' + f"{int(day):02}")
            stat = 1
    except ValueError:
            date = input(prompt)



main()
