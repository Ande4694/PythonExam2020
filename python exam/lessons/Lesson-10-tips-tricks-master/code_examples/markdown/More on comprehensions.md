# More on comprehensions

## List comprehension


```python
[i for i in range(1,10)]
```




    [1, 2, 3, 4, 5, 6, 7, 8, 9]



## Set comprehension


```python
{i for i in range(1, 10)}
```




    {1, 2, 3, 4, 5, 6, 7, 8, 9}



## Tuple comprehension
Remember that **(i for i in range(10))** is a generator expression.  
To create a tuple comprehension you will have to cast it.  


```python
tuple((i for i in range(10)))
```




    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)



## Dict comprehension


```python
d = [{"name": "Claus", "age": 120}, {"name": "ANna", "age": 32}]
{k:v for (k, v) in d.items()}]
```


      File "<ipython-input-15-674747163845>", line 2
        [i for i in d  {k:v for (k, v) in d.items()}]
                       ^
    SyntaxError: invalid syntax




```python
d = [{"name": "Claus", "age": 120}, ]
{k:v for (k, v) in d.items() }
```


```python

```
