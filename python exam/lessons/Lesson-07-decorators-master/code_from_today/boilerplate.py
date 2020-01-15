def decorator(func):
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        value = func(*args, **kwargs) // execute function
        # Do something after
        return value
    return wrapper_decorator
