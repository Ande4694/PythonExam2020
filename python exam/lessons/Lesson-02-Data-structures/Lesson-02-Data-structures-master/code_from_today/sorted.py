def last_char(s):
    return s[-1]



l = ['Claus', 'Anna', 'Henning']


j = sorted(l, key=last_char)

print(j)

