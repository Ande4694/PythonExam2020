# OpenFile.py


with open('../../testfiles/students.json', 'r') as f:
    print(f.readline())


with OpenFile('../../testfiles/students.json', 'r') as f:
    print(f.readline())