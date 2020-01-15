""" This function uses the concept of closure to preserve state. Like we know from Clases. """

def counter():
    x = 0 
    def add():
        nonlocal x
        x += 1
        return x
    return add


""" This would be the 'Normal' way to do it (preserve state) with a class """
class Counter:

    def __init__(self):
        self.__x = 0

    def __call__(self):
        self.__x += 1
        return self.__x


x = counter()
print(x())
print(x())
print(x())


x = Counter()
print(x())
print(x())
print(x())







