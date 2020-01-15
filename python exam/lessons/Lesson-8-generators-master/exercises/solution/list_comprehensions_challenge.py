""" 
    List Comprehension chalenges. 
    All the below exercieses, unless something else is stated, should be solved using: 
    * first a normal for loop, then a 

    * list comprehensions and a
    * a generator expression (where it makes sense)

    You should also run the 'timer' and 'memory usage' decorators on your new functions. 
    Try to see if you in anyway can optimize you code.
    (It is a good idea to test your solutions with large numbers and see how they react)

"""
# deocorator from lesson-07
import resource
import time

def memory(func):

    def wrapper(*args, **kwargs):
        # meassure memory before
        start_mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        
        # execute the script
        value =  func(*args, **kwargs)
        
        # meassure memory after
        end_mem = (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss) - start_mem
        
        print(f'Memory usage: {end_mem}')

        return value
        
    return wrapper    


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        value = func(*args, **kwargs)
        end = (time.time()) - start
        print(f'Time elapsed: {end}')
        return value

    return wrapper




# 1. Find all of the numbers from 1-1000 that are divisible by 7
@timer
@memory
def divisible_by_7(n):
    l = []
    for i in range(1, n):
        if i%7 == 0:
            l.append(i)
    return l

@timer
@memory
def divisible_by_7_comp(n):
    l1 = [i for i in range(n) if i%7==0]
    return l1




# 2. Find all of the numbers from 1-1000 that have a 3 in them


@timer
def three_in_num(n):
    l = []                                                                                                                  
    for i in range(n):
        if i % 10 == 3:                                                                                                             l.append(i)                                                                                                 
        elif i // 10 % 10 == 3:
            l.append(i)                                                                                                 
        elif i // 100 % 10 == 3:
            l.append(i)                                                                                                 
        elif i // 1000 % 10 == 3:
            l.append(i)  

    return l


@timer
def three_in_num_comp(n):
    # three_in_num_comp(100000000) takes 48.41 sek to execute
    #l = [i for i in range(n) if str(3) in str(i) ]

    # three_in_num_comp(100000000) takes 27.13 sek to execute
    l = [i for i in range(n) if i%10 == 3 or i // 10 %10 == 3 or i // 100 %10 == 3 or i//1000%10 == 3 ]
    
    return l


# 3. Count the number of spaces in a string

@timer
def number_spaces(s):
    # s = 'Hello World i am claus'
    count = 0
    for i in s:
        if i == ' ':
            count += 1

    return count

@timer
def number_spaces_comp(s):
    x = len([i for i in s if i == ' '])
    return x


# 4.  Remove all of the vowels in a string
@timer
def remove_vowels(s):
    v = {'a', 'e', 'i', 'o', 'u', 'y'}
    l = []
    for i in s:
        if i not in v:
            l.append(i)
    return ''.join(l)

@timer
def remove_vowels_comp(s):
    return ''.join([i for i in s if i not in  {'a', 'e', 'i', 'o', 'u', 'y'} ])    

@timer
def remove_vowels_gen(s):
    (i for i in s if i not in  {'a', 'e', 'i', 'o', 'u', 'y'} )


# 5.  In a string made up of randomly generated words, generate a list of all words that have less than 4 letters

# 6. Use a nested list comprehension to find all of the numbers from 1-1000 that are divisible by any single digit besides 1 (2-9)

# 7 . For all the numbers 1-1000, use a nested list comprehension to find the highest single digit any of the numbers is divisible by






# 8. Multiples of 3 and 5: If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.

@timer
def multiples_of_3_or_5(n):
    sum = 0    
    for number in range(n):
        if not number % 3 or not number % 5:
            sum += number
    return sum

@timer
def multiples_of_3_or_5_comp(n):
    return sum([i for i in range(n) if not i % 3 or not i % 5])

@timer
def multiples_of_3_or_5_gen(n):
        for number in range(n):
            if not number % 3 or not number % 5:
                yield number

x = sum(multiples_of_3_or_5_gen(1000))



 



