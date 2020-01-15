# reverce a text strig


def reverce(text):
    return text[::-1]

def reverce_with_methods(text):
    
    text = ''.join(reversed(text))
    return text


s  = reverce_with_methods('H there')


print(s)
    
