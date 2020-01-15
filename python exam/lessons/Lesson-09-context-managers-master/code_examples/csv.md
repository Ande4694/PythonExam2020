<h1>Reading and writing csv files<span class="tocSkip"></span></h1>
<div class="toc"><ul class="toc-item"><li><span><a href="#csv.reader()" data-toc-modified-id="csv.reader()-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>csv.reader()</a></span></li><li><span><a href="#csv.DictReader()" data-toc-modified-id="csv.DictReader()-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>csv.DictReader()</a></span></li><li><span><a href="#csv.writer()" data-toc-modified-id="csv.writer()-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>csv.writer()</a></span></li><li><span><a href="#csv.DictWriter()" data-toc-modified-id="csv.DictWriter()-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>csv.DictWriter()</a></span></li><li><span><a href="#Pandas" data-toc-modified-id="Pandas-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Pandas</a></span><ul class="toc-item"><li><span><a href="#read_csv()" data-toc-modified-id="read_csv()-5.1"><span class="toc-item-num">5.1&nbsp;&nbsp;</span>read_csv()</a></span></li></ul></li><li><span><a href="#10-minutes-exercise" data-toc-modified-id="10-minutes-exercise-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>10 minutes exercise</a></span></li></ul></div>

https://realpython.com/python-csv/  
https://realpython.com/working-with-large-excel-files-in-pandas/  

## csv.reader()


```python
import csv
```


```python
with open('testfiles/hrdata.csv', 'r') as f:
    csv_reader = csv.reader(f, delimiter=',')
    for row in csv_reader:
        print(row)

```

    ['Name', 'Hire Date', 'Salary', 'Sick Days remaining']
    ['Graham Chapman', '03/15/14', '50000.00', '10']
    ['John Cleese', '06/01/15', '65000.00', '8']
    ['Eric Idle', '05/12/14', '45000.00', '10']
    ['Terry Jones', '11/01/13', '70000.00', '3']
    ['Terry Gilliam', '08/12/14', '48000.00', '7']
    ['Michael Palin', '05/23/13', '66000.00', '8']


## csv.DictReader()


```python
with open('testfiles/hrdata.csv', 'r') as f:
    csv_reader = csv.DictReader(f)
    
    for row in csv_reader:
        print(row['Name'], row['Hire Date'], row['Salary'], row['Sick Days remaining'] )
```

    Graham Chapman 03/15/14 50000.00 10
    John Cleese 06/01/15 65000.00 8
    Eric Idle 05/12/14 45000.00 10
    Terry Jones 11/01/13 70000.00 3
    Terry Gilliam 08/12/14 48000.00 7
    Michael Palin 05/23/13 66000.00 8


## csv.writer()


```python
with open('testfiles/employee_file.csv', 'w') as f:
    employee_writer = csv.writer(f, delimiter=',')

    employee_writer.writerow(['John Smith', 'Accounting', 'November'])
    employee_writer.writerow(['Erica Meyers', 'IT', 'March'])
```


```python
with open('testfiles/employee_file.csv', 'r') as f:
    csv_reader = csv.reader(f, delimiter=',')
    for row in csv_reader:
        print(row)

```

    ['John Smith', 'Accounting', 'November']
    ['Erica Meyers', 'IT', 'March']


## csv.DictWriter()


```python
with open('testfiles/employee_file2.csv', 'w') as f:
    fieldnames = ['emp_name', 'dept', 'birth_month']
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader() # the fieldnames
    writer.writerow({'emp_name': 'John Smith', 'dept': 'Accounting', 'birth_month': 'November'})
    writer.writerow({'emp_name': 'Erica Meyers', 'dept': 'IT', 'birth_month': 'March'})
```


```python
with open('testfiles/employee_file2.csv', 'r') as f:
    csv_reader = csv.reader(f, delimiter=',')
    for row in csv_reader:
        print(row)
```

    ['emp_name', 'dept', 'birth_month']
    ['John Smith', 'Accounting', 'November']
    ['Erica Meyers', 'IT', 'March']


## Pandas


```python
import pandas
```

### read_csv()


```python
import pandas
df = pandas.read_csv('testfiles/hrdata.csv')
print(df)
```

                 Name Hire Date   Salary  Sick Days remaining
    0  Graham Chapman  03/15/14  50000.0                   10
    1     John Cleese  06/01/15  65000.0                    8
    2       Eric Idle  05/12/14  45000.0                   10
    3     Terry Jones  11/01/13  70000.0                    3
    4   Terry Gilliam  08/12/14  48000.0                    7
    5   Michael Palin  05/23/13  66000.0                    8


## 10 minutes exercise


```python

```
