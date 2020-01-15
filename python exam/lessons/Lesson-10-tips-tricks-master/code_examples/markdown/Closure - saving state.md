<h1>Closure - Saving state<span class="tocSkip"></span></h1>
<div class="toc"><ul class="toc-item"><li><span><a href="#The-'Normal'-way-to-preserve-state-with-a-class" data-toc-modified-id="The-'Normal'-way-to-preserve-state-with-a-class-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>The 'Normal' way to preserve state with a class</a></span></li><li><span><a href="#Closure" data-toc-modified-id="Closure-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Closure</a></span></li><li><span><a href="#Global,-Local-and-Nonlocal-variables" data-toc-modified-id="Global,-Local-and-Nonlocal-variables-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Global, Local and Nonlocal variables</a></span><ul class="toc-item"><li><span><a href="#Global-Variable" data-toc-modified-id="Global-Variable-3.1"><span class="toc-item-num">3.1&nbsp;&nbsp;</span>Global Variable</a></span><ul class="toc-item"><li><span><a href="#Changing-a-global-variable-inside-a-function-is-not-possible." data-toc-modified-id="Changing-a-global-variable-inside-a-function-is-not-possible.-3.1.1"><span class="toc-item-num">3.1.1&nbsp;&nbsp;</span>Changing a global variable inside a function is not possible.</a></span></li><li><span><a href="#Accessing-local-variable-outside-the-scope-is-also-not-possible." data-toc-modified-id="Accessing-local-variable-outside-the-scope-is-also-not-possible.-3.1.2"><span class="toc-item-num">3.1.2&nbsp;&nbsp;</span>Accessing local variable outside the scope is also not possible.</a></span></li><li><span><a href="#Using-Global-and-Local-variables-in-same-code" data-toc-modified-id="Using-Global-and-Local-variables-in-same-code-3.1.3"><span class="toc-item-num">3.1.3&nbsp;&nbsp;</span>Using Global and Local variables in same code</a></span></li></ul></li><li><span><a href="#Nonlocal-Variables" data-toc-modified-id="Nonlocal-Variables-3.2"><span class="toc-item-num">3.2&nbsp;&nbsp;</span>Nonlocal Variables</a></span></li></ul></li></ul></div>

## The 'Normal' way to preserve state with a class


```python
class Counter:
    def __init__(self):
        self.__x = 0

    def __call__(self):
        self.__x += 1
        return self.__x
```


```python
x = Counter()
print(x())
print(x())
print(x())
```

    1
    2
    3


## Closure
This function uses the concept of closure to preserve state. Like we know from Clases.


```python
def counter():
    x = 0           # a local variable
    def add():
        nonlocal x  # not a global and not a local 
        x += 1
        return x
    return add
```


```python
x = counter()
print(x())
print(x())
print(x())
```

    1
    2
    3


## Global, Local and Nonlocal variables

### Global Variable


```python
x = "global"

def foo():
    print("x inside :", x)

foo()
print("x outside:", x)
```

    x inside : global
    x outside: global


#### Changing a global variable inside a function is not possible.


```python
x = "global"

def foo():
    x = x * 2
    print(x)
# foo()
```

#### Accessing local variable outside the scope is also not possible.


```python
def foo():
    y = "local"

foo()
#print(y)
```

#### Using Global and Local variables in same code


```python
x = "global"

def foo():
    global x
    y = "local"
    x = x * 2
    print(x)
    print(y)
    
foo()
```

    globalglobal
    local


### Nonlocal Variables
Nonlocal variable are used in **nested function** whose local scope is not defined. This means, the variable can be neither in the local nor the global scope.  


```python
def outer():
    x = "local"
    
    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)
    
    inner()
    print("outer:", x)

outer()
```

    inner: nonlocal
    outer: nonlocal

