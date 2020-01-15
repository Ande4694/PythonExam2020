# Lambda expression

## Simple example
### normal function


```python
def identity(x):
    return x
```

### Lambda expression
We do not have a name to call here. It is an **anonomous function.**


```python
lambda x: x
```




    <function __main__.<lambda>(x)>



### multiple parameters


```python
lambda x, y: x + y
```




    <function __main__.<lambda>(x, y)>



## Immediately Invoked Function Expression (IIFE)


```python
(lambda x, y: x+y)(2,3)
```




    5



## Anonomous function
Lambda is an anonomous function, but you can name is by:  


```python
multiply = lambda x, y : x * y
multiply(2, 13)
```




    26



## lambda as key in sorting


```python
students = [('john', 'A', 22),('jane', 'B', 32),('dave', 'B', 21)]
sorted(students, key=lambda student: student[2]) # sort by age
```




    [('dave', 'B', 21), ('john', 'A', 22), ('jane', 'B', 32)]



##  Using dictionary and a lambda as a switch


```python
def calculate(*args):
    dict = {'+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '/': lambda a, b: a / b,
            '*': lambda a, b: a * b
            }[args[1]](args[0], args[2])
    return dict


calculate(2, '*', 5)
```




    10



## 10 minutes Lambda exercise


```python

```
