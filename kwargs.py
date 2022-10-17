# kwargs = parameter that will pack al arguments into a dictionary

def hello(**kwargs):
    print("hello", end=" ")
    for key, value in kwargs.items():
        print(value, end=" ")

hello(first="Lee", second="Kschi")