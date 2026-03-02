import re

def main():
    print(convert(input("Hours: ")))


def convert(s):
    if hours := re.search(r"^(1?\d)(:[0-5]\d)? (AM|PM) to (1?\d)(:[0-5]\d)? (AM|PM)$", s):
        hour_start = hours.group(1)
        hour_end = hours.group(4)
        minutes_start = hours.group(2)
        minutes_end = hours.group(5)
        if minutes_start == None:
            minutes_start = ":00"
        if minutes_end == None:
            minutes_end = ":00"

        if hours.group(3) == "AM" and hours.group(6) == "PM":
            if (0 < int(hour_start) < 13) and (0 < int(hour_end) < 13):
                if (hour_start and hour_end) == "12":
                    return f"00{minutes_start} to {hour_end}{minutes_end}"
                return f"{hour_start.zfill(2)}{minutes_start} to {int(hour_end)+12}{minutes_end}"


        elif hours.group(3) == "PM" and hours.group(6) == "AM":
             if (0 < int(hour_start) < 13) and (0 < int(hour_end) < 13):
                if (hour_start and hour_end) == "12":
                    return f"00{minutes_start} to {hour_end}{minutes_end}"
                return f"{int(hour_start)+12}{minutes_start} to {hour_end.zfill(2)}{minutes_end}"

        elif hours.group(3) == "PM" and hours.group(6) == "PM":
             if (0 < int(hour_start) < 13) and (0 < int(hour_end) < 13):
                if (hour_start and hour_end) == "12":
                    return f"00{minutes_start} to {hour_end}{minutes_end}"
                return f"{int(hour_start)+12}{minutes_start} to {int(hour_end)+12}{minutes_end}"
        else:
            return f"{hour_start}{minutes_start} to {hour_end}{minutes_end}"
        raise ValueError("Wrong value")
    else:
        raise ValueError("Wrong value")


if __name__ == "__main__":
    main()
