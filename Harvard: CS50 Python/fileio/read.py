with open("names.txt", "r") as file:
    lines = file.readlines()
    
for line in lines:
    #print always add new line 
    print("hello,", line.rstrip())