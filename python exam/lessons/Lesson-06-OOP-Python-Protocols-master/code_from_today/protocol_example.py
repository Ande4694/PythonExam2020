class S:

    def __init__(self):
        self.name = 'Claus'
        self.sir = 'Bove'

    def __repr__(self):
        return str(self.__dict__)


    def __str__(self):
        return self.name

    def __add__(self, other):
        return  self.name + other.name

    def __call__(self):
        return 'blablabl'
