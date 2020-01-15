# Pickle - Python object serialization

When "pickel-ing" you convert a python object into bytecode and then you can save that to a file etc.  
You use [dumps()](https://docs.python.org/3/library/pickle.html#pickle.dumps) for serializing and [loads()](https://docs.python.org/3/library/pickle.html#pickle.loads) for de-serializing the object.  


```python
l = [i for i in range(10)]
```

## dumps()


```python
import pickle as p
picl = p.dumps(l)
picl
```




    b'\x80\x03]q\x00(K\x00K\x01K\x02K\x03K\x04K\x05K\x06K\x07K\x08K\te.'




```python
with open('testfiles/list.pickle', 'bw') as f:
    f.write(picl)
```


```python
with open('testfiles/list.pickle', 'br') as f:
    out = f.read()
out
```




    b'\x80\x03]q\x00(K\x00K\x01K\x02K\x03K\x04K\x05K\x06K\x07K\x08K\te.'



## loads()


```python
p.loads(out)
```




    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]



## Try to save a non-serialized object


```python
with open('testfiles/list.txt', 'w', encoding='utf8') as f:
    f.write(l)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-26-68e8fb8dafc7> in <module>
          1 with open('testfiles/list.txt', 'w', encoding='utf8') as f:
    ----> 2     f.write(l)
    

    TypeError: write() argument must be str, not list

