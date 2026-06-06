def announce(func):
    def wrapper():
        print("Calling function")
        return func()
    return wrapper

@announce
def greet():
    print("Hello")

greet()
