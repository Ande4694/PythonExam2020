#iterator.py

for i in [1,2,3,4]:
    print(i)




class MyIterator:
    def __init__(self, *args):
       pass
       
       
my_iter = MyIterator(6)
for i in my_iter:
    print(i)