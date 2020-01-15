# compute.py

from time import sleep
"""
def compute():
    l = []
    for i in range(10000000):
        sleep(.5)
        l.append(i)
    return l
"""
"""

for x in xs:
    pass

i = iter(xs)
while True:
    next(i)

StopIteration

"""

def compute():
    for i in range(1000000):
        sleep(.5)
        yield i

class Compute:
    """
    def __call__(self):

        l = []
        for i in range(10):
            sleep(.5)
            l.append(i)
    return l
    """
    def __iter__(self):
        self.start = 0
        return self

    def __next__(self):
        if self.start > 10:  
            raise StopIteration()

    
        sleep(.5)
        self.start -= 1
        return self.start

comp = Compute()






