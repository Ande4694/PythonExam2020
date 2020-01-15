# Context managers

You all seen the pattern: 


```python
with open('testfiles/bohr.txt', 'r') as f:
    f.readline
```

This is a convenient alternative to writing:


```python
try:
    f = open('testfiles/bohr.txt', 'r')
    print(f.readline())
finally:
    f.close()
```

    An expert is a person who has made all the mistakes that can be made in a very narrow field.
    


We will look at how this works, and we will write or own Context manager that follow the protocol. 

The problem with not closing files can be demonstarted like this:


```python
# do not run this on windows

files = []
for x in range(1000):
    files.append(open('testfiles/bohr.txt', 'r'))

# You will get an error about to many open files.
```

## Basic Context Managers
The context manager protocol consists of an **\_\_enter__** and an **\_\_exit__** method.  
when using the **with** statement the **\_\_enter__** method is called.  
What is in the scope is executed and  
The **\_\_exit__** method is called when leaving the scope.  


```python
class OpenFile():
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print('__enter__')
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, *args):
        print('__exit__')
        self.file.close()


with OpenFile('testfiles/bohr.txt', 'r') as f:
    print(f.readline())
```

    __enter__
    An expert is a person who has made all the mistakes that can be made in a very narrow field.
    
    __exit__


### contextlib
The contextlib module consists of different context manager.  
We will look at 2 of them.  

**@contextmanager**
> A decorator that lest you build a context manager from a simple generator function, instead of creating a class and implementing the protocol.  

**ContextDecorator**
> A base class for defining class-based context managers that can also be used as function decorators, running the entire function within a managed context. 


```python
from contextlib import contextmanager

@contextmanager
def open_file(filename, mode):
    f = open(filename, mode)
    try:
        yield f
    finally:
        f.close()
```

####  Pseudo code of the decorator


```python
def contextmanager(func):
    def inner(filename, mode):
        # __enter__
        # retturns a file object.  A stopiteration is raised
        value = func(filename, mode)

        # __exit__
        next(value)  # raise a StopIteration and execute finally clause
        return value  # value is a generator
    return inner  # inner function returns a generator


def open_file(filename, mode):
    f = open(filename, mode)
    try:
        print('in try')
        yield f
    finally:
        print('in finally')
        f.close()


open_file = contextmanager(open_file)

x = open_file('testfiles/bohr.txt', 'r')
print(next(x))
```

    in try
    in finally



    ----------------------------------------------------------------

    StopIteration                  Traceback (most recent call last)

    <ipython-input-8-eb5c2605a35f> in <module>
         21 
         22 x = open_file('testfiles/bohr.txt', 'r')
    ---> 23 print(next(x))
    

    StopIteration: 


## ContextDecorator


```python
from contextlib import ContextDecorator

class makeparagraph(ContextDecorator):
    def __enter__(self):
        print('<p>')
        return self

    def __exit__(self, *arg):
        print('</p>')
        return False

@makeparagraph()
def emit_html(msg):
    print(msg)

emit_html('Hello World')
```

    <p>
    Hello World
    </p>


### Decorator function


```python
def makeparagraph(func):
    def inner_decorator(*args, **kwargs):
        print("<p>")
        func(*args, **kwargs)
        print("</p>")
    return inner_decorator


@makeparagraph
def greetings(msg):
    print(msg)


greetings('Hello world')
```

    <p>
    Hello world
    </p>

