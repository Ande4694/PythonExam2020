class A:
    # 1st example
    def __init__(self):
        self.__a = 'A'        # public
        self.b = 'B'        # public

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, x):
        if type(x) == int:
            print('NO nO')
        else:
            self.__a = x
