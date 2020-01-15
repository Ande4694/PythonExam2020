# meny.py meny functions

import sys
plugins = {}    # dict with function name as key and function as value
                # {'home' : home, 'about' : about}

def register(func):
    """Register a function as a plug-in"""
    plugins[func.__name__] = func
    return func


@register
def home():
    return f'Im the HOME functionality'

@register
def about():
    return f'Im the ABOUT functionality'

@register
def contact():
    return f'Im the CONTACT functionality'

@register
def quit():
    sys.exit()

@register
def webshop():
    return f'Im the WEBSHOP'
@register
def test():
    return 'Im the TEST'
