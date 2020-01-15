
# Teaching notes OOP in python

## Declaration of a class


```
class Person:
    pass
```

create an instance of the class
```
p = Person()
```
## Creating a constructor


```
class Person:
    def __init__(self):
        pass
```

The init method and any other method should always have __self__ as a first parameter.

## Instance and class variables

Instance attributes are defined in the __init__ method or in another method.  
They are denoted with the __self__ prefix. 


```
class Person:
    def __init__(self, name):
        self.name = name # -> instance method
```

Class methods can be defined outside any method, but inside the class scope, or inside methods. Typically you will declare them as the firt elements after the class declaration line. They are not denoted by __self__, and they are shared by all object created from the class. 


```
class Person:
    
    type = 'Mammel' # class variable (no self in front of)
    
    def __init__(self, name):
        pass
```

Class variables can also be constructed through methods


```
class Person:  
    def __init__(self, type):
        Person.type = type
```

**Eksample:**


```
p = Person('Mammel')
```


```
p.type
```




    'Mammel'




```
s = Person('Reptile')
```


```
s.type
```




    'Reptile'




```
p.type
```




    'Reptile'



### Add / Change instance variables after declaration
You can at runtime add variables (and methods) to your object


```
p = Person('Claus')
```


```
p.__dict__   # __dict__ is used to get a dictionary of all instance variables
```




    {}




```
p.age = 23
p.sirname = 'Henningen'
```


```
p.__dict__
```




    {'age': 23, 'sirname': 'Henningen'}



### Add / Change class variables after declaration


```
Person.name = 'Kim'
```

**Eksample:**


```
class Animal:
    name = 'Fido'
```


```
dog = Animal()
cat = Animal()
```


```
dog.name
```




    'Fido'




```
cat.name
```




    'Fido'




```
Animal.name = 'Esther'
```


```
dog.name
```




    'Esther'




```
cat.name
```




    'Esther'



## @Overloading
You can read more about this [here]()
and *args and **kwargs [here](https://realpython.com/python-kwargs-and-args/)

Overloading in python is done by using the *args, and **kwargs arguments


```
def __init__(self, *args):
    if len(args) == 1:
        self.name = args[0]
    elif len(args) == 2:
        self.name = args[0]
        self.sirn = args[1]
    else:
        raise NotImplemented
```

# Inheritance


```
class Person:
    def __init__(self, name):
        self.name = name
```


```
class Student(Person):
    def __init__(self, name):
        super().__init__(name)
```


```
s = Student('Claus')
```

This approach is also valid


```
class Student(Person):
    def __init__(self, name):
        Person.__init__(self, name)
```


```
s = Student('Claus')
```

### Mutiple inheritance
In Python You can inherite from multible classes


```
class Instructurer:
    def __init__(self, course):
        pass
        
class Student(Person, Instructurer):
    def __init__(self, name, course):
        Person.__init__(self, name)
        Instructurer.__init__(self, course)
        
s = Student('Claus', 'Co23')
```

## Private members


```
class P:
   def __init__(self, name, alias):
      self.name = name       # public
      self.__alias = alias   # private

   def who(self):
      print('name  : ', self.name)
      print('alias : ', self.__alias)
```


```
p = P('Claus', 'clbo')
p.who()
```

    name  :  Claus
    alias :  clbo


Trying to access p.alias -&gt; attribut does not exist


```
p.name
p.alias
```

```
    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-64-80130101ca26> in <module>
          1 p.name
    ----> 2 p.alias
    

    AttributeError: 'P' object has no attribute 'alias'



```
Since __alias is private Trying to access p.alias -> attribut does not exist
```


      File "<ipython-input-65-26b222f527ab>", line 1
        Since __alias is private Trying to access p.alias -> attribut does not exist
                    ^
    SyntaxError: invalid syntax




```
p.__alias
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-66-f640b37f79a1> in <module>
    ----> 1 p.__alias
    

    AttributeError: 'P' object has no attribute '__alias'

```
You can access an objects private attributes like this  
This is why you sometimes will hear that private does not realy exists in python.  


```
p._P__alias
```


```
'clbo'
```

