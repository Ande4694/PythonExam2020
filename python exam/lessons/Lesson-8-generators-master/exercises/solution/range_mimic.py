# range_mimic.py

# 1. Create a "clone" of the build in range() function.

class MyRange:

    def __call__(self, *args):
        if len(args) == 1:
            self.start = 0
            self.end = args[0]
            self.step = 1
        elif len(args) == 2:
            self.start = args[0]
            self.end = args[1]
            self.step = 1
        elif len(args) == 3:
            self.start = args[0]
            self.end = args[1]
            self.step = args[2]
        return iter(self)

    def __iter__(self):
        self.i = self.start
        return self

    def __next__(self):
        try:
            if self.end > self.i:
                self.tmp = self.i
                self.i += self.step
                return self.tmp
            else:
                raise StopIteration
        except AttributeError:
            raise TypeError('range method is not itterable')


my_range = MyRange()
x = my_range(2, 6)
for i in x:
    print(i)


# 2. Now do the same, but use a generator function instead.

