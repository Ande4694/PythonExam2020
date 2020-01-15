<h1>Working With JSON Data in Python<span class="tocSkip"></span></h1>
<div class="toc"><ul class="toc-item"><li><span><a href="#Reading-JSON" data-toc-modified-id="Reading-JSON-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Reading JSON</a></span><ul class="toc-item"><li><span><a href="#json.load" data-toc-modified-id="json.load-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>json.load</a></span></li><li><span><a href="#json.loads" data-toc-modified-id="json.loads-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>json.loads</a></span></li></ul></li><li><span><a href="#Writing-JSON" data-toc-modified-id="Writing-JSON-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Writing JSON</a></span><ul class="toc-item"><li><span><a href="#json.dumps" data-toc-modified-id="json.dumps-2.1"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>json.dumps</a></span></li><li><span><a href="#json.dump" data-toc-modified-id="json.dump-2.2"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>json.dump</a></span></li></ul></li><li><span><a href="#10-minutes-exercise" data-toc-modified-id="10-minutes-exercise-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>10 minutes exercise</a></span></li></ul></div>

https://realpython.com/python-json/
https://docs.python.org/3/library/json.html

## Reading JSON


```python
import json
```

### json.load
Reads from a file path


```python
with open('testfiles/animals.json', 'r') as f:
    json_list = json.load(f)  

print(json_list)
```

    [{'animal': {'name': 'Henning', 'species': 'House Cat', 'relatives': [{'name': 'Fluffy', 'species': 'Norwegian Forrest'}]}}, {'animal': {'name': 'Fido', 'species': 'Dog', 'relatives': [{'name': 'Jeff', 'species': 'Puddle'}, {'name': 'Minna', 'species': 'Labrador'}]}}]



```python
[i['animal']['name'] for i in json_list]
```




    ['Henning', 'Fido']



### json.loads
Reads the content of the file


```python
with open('testfiles/animals.json', 'r') as f:
    txt = f.read()
    js = json.loads(txt)
    
print(js)
```

    [{'animal': {'name': 'Henning', 'species': 'House Cat', 'relatives': [{'name': 'Fluffy', 'species': 'Norwegian Forrest'}]}}, {'animal': {'name': 'Fido', 'species': 'Dog', 'relatives': [{'name': 'Jeff', 'species': 'Puddle'}, {'name': 'Minna', 'species': 'Labrador'}]}}]



```python
[i['animal']['relatives'] for i in js]
```




    [[{'name': 'Fluffy', 'species': 'Norwegian Forrest'}],
     [{'name': 'Jeff', 'species': 'Puddle'},
      {'name': 'Minna', 'species': 'Labrador'}]]



## Writing JSON

### json.dumps
Serialize obj to a JSON formatted str


```python
dict = {'name' : 'Claus', 'age' : 120}
with open('testfiles/students.json', 'w') as f:
    js =json.dumps(dict)
    f.write(js)
```


```python
with open('testfiles/students.json', 'r') as f:
    js = json.load(f)  
print(js)
```

    {'name': 'Claus', 'age': 120}


### json.dump
Serialize obj as a JSON formatted stream to fp (a .write()-supporting file-like object)


```python
from io import StringIO
io = StringIO()
teachers = [{'name' : 'Claus', 'age' : 120}, {}]
with open('testfiles/teachers.json', 'w') as f:
    json.dump(dict, io)
    f.write(io.getvalue())
```


```python
with open('testfiles/teachers.json', 'r') as f:
    js = json.load(f)  
print(js)
```

    {'name': 'Claus', 'age': 120}


## 10 minutes exercise 

1. From this api https://api.github.com/orgs/python-elective-fall-2019/repos get all names of the repos and write them to a text file.  

2. Get all filenames of files ending with **.ipynb** in the **code_examples** folder in the Lesson-09-context-managers repository. 


```python

```
