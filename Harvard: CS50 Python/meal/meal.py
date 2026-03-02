#breakfast between 7:00 and 8:00, lunch between 12:00 and 13:00, and dinner between 18:00 and 19:00.

#breakfast time, lunch time, or dinner time.

def main():

    time = input("What time it is? ")
    convert(time)

    if ready_time <= float(8.00) and ready_time >= float(7.00):
        print('breakfast time')
    elif ready_time >= 13.00 and ready_time <= 14.00:
        print("lunch time")
    elif ready_time >= 18.00 and ready_time <= 19.00:
        print("dinner time")
    else:
        return 0

def convert(time):
    time = time.replace(":", ".").split(".")
    after_point = (int(time[1])*100)/60
    time[1] = int(after_point)
    time = time[0]+"."+str(time[1])
    global ready_time
    ready_time = float(time)
    return ready_time



if __name__ == "__main__":
    main()