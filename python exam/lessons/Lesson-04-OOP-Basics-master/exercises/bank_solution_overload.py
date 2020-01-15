""" Bank Exercise 

Create a 

* Bank class
* Account Class
* Customer class

The bank class should be able to hold many account.
You should be able to add new accounts.
The Account class should have relevant details.
The Customer class Should also have relevant details.

Stick to the techniques we have covered so far.


"""

class Bank:
    def __init__(self, acc):
        self.accounts = []
        self.accounts.append(acc)




class Account:
    def __init__(self, no, cust):
        self.no = no
        self.cust = cust

    


class Customer:
    def __init__(self, name):
        self.name = name

"""
## Overloading
Add the abillity in your code to overload one or more init methods
"""

class Customer:
    def __init__(self, *args):
        if len(args) == 1:
            self.name = args[0]

      elif len(args) == 2:
            self.name = args[0]
            self.age = args[1]
      else:
            self.name = args[0]
            self.age = args[1]
            self.gender = [2]

















