# Tips & Tricks

## Unpacking With the Asterisk Operators: * & **

You can use the * sign to unpack a list, tuple or set etc.


```python
# print_unpacked_list
my_list = [1, 2, 3]
print('List: ', *my_list)

# print_unpacked_set
my_set = {3, 4, 5}
print('Set: ', *my_set)

# print_unpacked_tuple
my_set = (13, 14, 15)
print('tuple: ', *my_set)
```

    List:  1 2 3
    Set:  3 4 5
    tuple:  13 14 15


This tequnique can be used as the following


```python
# unpacking_call
def my_sum(a, b, c):
    print(a + b + c)

my_list = [1, 2, 3]
my_sum(*my_list)
```

    6


## You can use the ** sign to unpack a dict


```python
d = {'a': 1, 'b': 3, 'c': 4}
def add(*args, **kwargs):
    print('args: ', args)
    print('kwargs :', kwargs)

add(d)
add(**d)
```

    args:  ({'a': 1, 'b': 3, 'c': 4},)
    kwargs : {}
    args:  ()
    kwargs : {'a': 1, 'b': 3, 'c': 4}


### Merging dictionaries


```python
x = {'a': 1, 'b': 3}
y = {'b': 2, 'c': 4}

z = {**x, **y}

z
```




    {'a': 1, 'b': 2, 'c': 4}



### Dict of functions
https://realpython.com/instance-class-and-static-methods-demystified/#lets-see-them-in-action
The concept og caling methods on an object vs. passing in an object to the class


```python
class A:
    def __init__(self, name):
        self.name = name

    def message(self):
        return 'Hi ' + self.name


fun_dict = {}
    
for k, v in A.__dict__.items():
    if callable(v) and k[:2] != '__':
            fun_dict[k] = v
            
fun_dict
```




    {'message': <function __main__.A.message(self)>}




```python
a = A('Ole')            
fun_dict['message'](a)
```




    'Hi Ole'




```python
dir(a)
```




    ['__class__',
     '__delattr__',
     '__dict__',
     '__dir__',
     '__doc__',
     '__eq__',
     '__format__',
     '__ge__',
     '__getattribute__',
     '__gt__',
     '__hash__',
     '__init__',
     '__init_subclass__',
     '__le__',
     '__lt__',
     '__module__',
     '__ne__',
     '__new__',
     '__reduce__',
     '__reduce_ex__',
     '__repr__',
     '__setattr__',
     '__sizeof__',
     '__str__',
     '__subclasshook__',
     '__weakref__',
     'message',
     'name']




```python
[i for i in dir(a) if callable(getattr(a, i)) and i[:2] != '__']
```




    ['message']




```python
A.message(A('Claus'))
```




    'Hi Claus'


