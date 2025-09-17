
# decorator? : wrapping around something fancy...


# A method that takes another method as parameters

def my_decorator(func):
    def abc(*args, **kwargs):
        print("Hello")
        func(*args, **kwargs)
        print("Goodbye")
    return abc


def my_decorator_2(func):
    def abc(*args, **kwargs):
        print("Hello finally")
        func(*args, **kwargs)
        print("Goodbye finally")
    return abc

def greet(name):
    print(name)

@my_decorator
@my_decorator_2
def say_hello(name):
    print(name)


if __name__ == "__main__":
    say_hello("John")
