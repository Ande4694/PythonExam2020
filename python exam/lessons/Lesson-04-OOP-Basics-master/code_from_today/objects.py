
class Person:
   
    #type = 'Mammel' 

    # Constructor
    #def __init__(self, name):
    #    self.name = name  #Instance variable 

    
    """
    def __init__(self, *args):

        if len(args) == 0:
            pass
        elif len(args) == 1:
            self.name = args[0]

        else:
            self.name = args[0]
            self.age = args[1]

    """

    def __init__(self, name = None, age = None):
        self.name = name
        self.age = age


    def __init__(self):
        pass


# p = Person('Claus', 'Reptile')




