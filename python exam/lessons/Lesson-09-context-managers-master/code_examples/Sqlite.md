# Connect and use an SQLite database

## Create, insert and read


```python
from sqlite3 import connect

with connect('testfiles/school.db') as conn:
    cur = conn.cursor()
    cur.execute('CREATE TABLE students(id int PRIMARY KEY, name text, cpr text)')
    cur.execute('INSERT INTO students(id, name, cpr) VALUES (1, "Claus", "223344-5566")')
    cur.execute('INSERT INTO students(id, name, cpr) VALUES (2, "Julie", "111111-1111")')
    cur.execute('INSERT INTO students(id, name, cpr) VALUES (3, "Hannah", "222222-2222")')
    for i in cur.execute('SELECT * FROM students'):
        print(i)
        
    cur.execute('DROP TABLE students')
```

    (1, 'Claus', '223344-5566')
    (2, 'Julie', '111111-1111')
    (3, 'Hannah', '222222-2222')


A more low level description can be found [here](https://www.sqlitetutorial.net/sqlite-python/creating-database/)

## 10 minutes exercise

1. Create a zoo database with a table animal. Insert some animals, update the information, and delete som animals
2. Add a table 'animal_groups'. Relate the animal table to the animal_groups table.  


```python

```
