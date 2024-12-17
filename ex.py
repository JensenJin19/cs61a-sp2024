def func2(func):
    def func3():
        print("Before calling func1")
        func()  # Call the original func1
        print("After calling func1")
    return func3

@func2  # Decorate func1 using decorator func2
def func1():  # Completely equivalent to: func1 = func2(func1)
    print("This is func1")