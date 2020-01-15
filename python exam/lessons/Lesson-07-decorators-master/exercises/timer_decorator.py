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
    
    Exercise 1:
    The first thing you should do is to define a function that takes a 'number' parameter and returns a list of number in the range from 1 to the number from the parameter.  


    Exercise 2:
    Requirements has changed and now you need to be able to meassure the execution time of the the function.
    Your job is, if you choose to accept the task, to write a decorator function that can time any piece of code.

    You can read about time by starting your interpretor and write:

        > import time
        > help(time)

    
    
    Exercise 3:
    New requirements. You need to be able to check memory usage of any script. 
    To check memory usage of a script you can do something like this:

        > start_mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        > end_mem = (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss) - start_mem

    And you can read about the resource module by starting your interpretor and write:

        > import resource 
        > help(resource)

"""

