import resource
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

@memory
def gen_fibonacci(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        #vi sætter:
        #a til at være lige med b
        #b = sum af forrige a+b
        a,b = b,a + b
        
@memory
def gen_fibon(n):
    a = 1
    b = 1
    output = []
    for s in range(n):
        output.append(a)
        a,b = b,a+b
    return output


print(gen_fibonacci(10))
print(gen_fibon(10))
