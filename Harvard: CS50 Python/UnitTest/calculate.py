def main():
    x  = int(input("What's x? "))
    print("x squared", square(x))
    return f"this is {x}" 
    
    
def square(n):
    return n * n
    

if __name__ == "__main__":
    main()