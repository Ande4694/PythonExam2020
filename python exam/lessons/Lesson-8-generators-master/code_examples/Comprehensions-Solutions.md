# Comprehensions in Python

Comprehensions in Python provide us with a short and concise way to construct new sequences (such as lists, set, dictionary etc.) using sequences which have been already defined. Python supports the following 4 types of comprehensions:

* List Comprehensions
* Dictionary Comprehensions
* Set Comprehensions
* Generator Comprehensions (Generator expressions)  

## List Comprehensions:  
List Comprehensions provide an elegant way to create new lists.  
The following shows the basic structure of a list comprehension:

<div style="text-align: right"><small><i>&copy; https://www.geeksforgeeks.org/comprehensions-in-python/</i></small></div>

l = [x for x in [1, 2, 3, 4]]
l

So a for loop looking like this:


```python
l = []
for i in range(1, 10):
    l.append(i)
l
```




    [1, 2, 3, 4, 5, 6, 7, 8, 9]



Could be written like this:


```python
l = [i for i in range(1, 10)]
l
```




    [1, 2, 3, 4, 5, 6, 7, 8, 9]



### if, else, elif 

#### if
Comprehensions can contain if conditions.  
The following shows the basic structure of a list comprehension containig an if condition:


```python
l = [i for i in range(1, 10) if i%2 == 0]
l
```




    [2, 4, 6, 8]



#### if / else
Comprehensions can contain if / else conditions.  
The following shows the basic structure of a list comprehension containig an if / else condition:


```python
[i if i%2 == 0 else "un-even" for i in range(1, 10) ]
```




    ['un-even', 2, 'un-even', 4, 'un-even', 6, 'un-even', 8, 'un-even']



## STUDENTS 10 MINUTES TASK
#### elif

Comprehensions can contain elif conditions.   
The following shows the basic structure of a list comprehension containig a elif condition:  


```python
[i if i%2 == 0 else 'un-even and small' if i < 5 else 'un-even and large' for i in range(1, 10)]
```




    ['un-even and small',
     2,
     'un-even and small',
     4,
     'un-even and large',
     6,
     'un-even and large',
     8,
     'un-even and large']



## Nested for loops
Like you can do a nested for loop


```python
l = []
for i in range(5):
    for j in range(i):
        l.append((i, j))
l
```




    [(1, 0),
     (2, 0),
     (2, 1),
     (3, 0),
     (3, 1),
     (3, 2),
     (4, 0),
     (4, 1),
     (4, 2),
     (4, 3)]



You can do the same with list comprehensions


```python
[(i, j) for i in range(5) for j in range(i)]
```




    [(1, 0),
     (2, 0),
     (2, 1),
     (3, 0),
     (3, 1),
     (3, 2),
     (4, 0),
     (4, 1),
     (4, 2),
     (4, 3)]



### STUDENTS 10 MINUTES TASK

From 2 lists, using a list comprehension, create a list containing:
[(Black, s), (Black, m), (Black, l), (Black, xl), (White, s), (White, m), (White, l), (White, xl)]

```python
colors = ['Black', 'White']
sizes = ['s', 'm', 'l', 'xl']
```


```python
# exercise
[(x,y) for y in sizes for x in colors]
```




    [('Black', 's'),
     ('White', 's'),
     ('Black', 'm'),
     ('White', 'm'),
     ('Black', 'l'),
     ('White', 'l'),
     ('Black', 'xl'),
     ('White', 'xl')]



## Nested list comprehension
Comprehensions can contain nested comprehensions.  
The following shows the basic structure of a list comprehension containig a list comprehension:


```python
[(i, j) for i in [j for j in range(i)]]
```




    [(0, 3), (1, 3), (2, 3), (3, 3)]


