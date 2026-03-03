
s = 'uobobovbobbbojwgjobobobooxobobobo'
count = 0
start = 0

while start < len(s):


    pos = s.find("bob", start)
    #if exist
    if pos != -1:
        start = pos + 1
        count += 1
    else:
    # If no further substring is present
        break


print("Number of times bob occurs is: ", count)