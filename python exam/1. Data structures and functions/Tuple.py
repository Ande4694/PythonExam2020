#Tuple


#*args og **kwargs & decorators
def quotes(*args):
    for _ in args:
        print(_)

def text_file_decorator(func):
    def inner(*args):
        with open('bohr.txt', 'r') as f:
            func(''.join(f.readlines())) # or *list -> list unpacking
    return inner

@text_file_decorator
def quotes_with_deco(*args):
    for _ in args:
        print(_)

quotes_with_deco()

def args_example(*args):
    print(args[0])
    print(args)

args_example('hej', 3, 6)

def kwargs_example(**kwargs):
    if 'hej' in kwargs:
        print(kwargs['hej'])
    else:
        print('ikke hej')

kwargs_example(hej='claus er lidt sløj')
kwargs_example(hey='hey der', ty='123', hyp='123', op=123)


def tuple_example():
    return 'sigurd'

def argsOgKwargs(*args, **kwargs):
    print(args[1])
    print(kwargs['hej'])

argsOgKwargs(2,tuple_example(),5, hej='frugtskål')


