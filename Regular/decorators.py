def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Don with function.")

    return wrapper


@announce
def hello():
    print("Hello")


hello()
