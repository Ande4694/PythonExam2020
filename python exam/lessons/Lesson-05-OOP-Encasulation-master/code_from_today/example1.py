class P:
    def __init__(self, name, alias):
        self.__name = name       # private
        self.__alias = alias   # private

    # getter
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if 'A' in name:
            self.__name = name


"""
    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

"""
"""
p = P('Claus', 'clbo')

p2 = P('Anna', 'ann')


p.setName(p.getName() + p2.getName())

p.name = p.name + p2.name
"""


















