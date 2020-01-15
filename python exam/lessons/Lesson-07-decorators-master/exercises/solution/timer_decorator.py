""" 
    Timer_memory_measure_deocator_function
    
    On next monday we will work with generators, generator expressions and list comprehensions. 
    These topics has a lot to do with program efficiency. 

    For this we will be measuring or code examples in diffenrent ways and espialy we will time it and messure memmory usage. 

    Instead of writing:

    start = time.time()
    // do some stuff here
    end = time.time()
    print(end - start)

    every time we need to time something, we could write a docorator function that does the job for us. 

    Your job is, if you choose to accept the task, to write a decorator function that can time any piece of code, and another decorator function that can meassure the memory load. 


    You can read about time by starting your interpretor and write:

        > import time
        > help(time)

    To check memory usage of a script you can do something like this:

        > start_mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        > end_mem = (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss) - start_mem

    And you can read about the resource module by starting your interpretor and write:

        > import resource 
        > help(resource)

"""

import resource
import time

def memory(func):

    def wrapper(*args, **kwargs):
        # meassure memory before
        start_mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        
        # execute the script
        func(*args, **kwargs)
        
        # meassure memory after
        end_mem = (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss) - start_mem
        
        print(f'Memory usage: {end_mem}')
        
    return wrapper    

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = (time.time()) - start

        print(f'Time elapsed: {end}')

    return wrapper


@timer
@memory
def genrate_list(num):
    [x for x in range(1, num)]

