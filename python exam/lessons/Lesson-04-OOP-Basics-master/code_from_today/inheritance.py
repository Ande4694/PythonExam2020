# inheritance.py

class Person:
    def __init__(self, name):
        self.name = name
"""

class Student(Person):
    def __init__(self, name, id):
        super().__init__(name)
        self.id = id


class Teacher(Person):
    def __init__(self, name, skills):
        Person.__init__(self, name)
        self.skills = skills

    def display(self):
        return self.skills + self.name 

"""

class Instructor:
    def __init__(self, course):
        self.course = course

class Student(Person, Instructor):
    def __init__(self, name, course):
        Person.__init__(self, name)
        Instructor.__init__(self, course)









