

def my_decorator(func):
    
    def wrapper(*args, **kwargs): # tuple   -> ('Claus', 'hans')
        # Before do something
        value = nunc(*args, **kwargs)
        # After do something
        return value
    return wrapper

@my_decorator
def greet(*args):
    return f'Hello {args[:]}'

@my_decorator
def action(*args):
    return 'Hello Hello'









"""
greet = decorator(greet)
greet()


@property
def main():


main = property(getx, setx, delx, 'Im a property')



"""




