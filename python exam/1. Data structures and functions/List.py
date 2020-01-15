#lists

#Simple list
a = ['foo', 'bar', 'baz', 'qux']
print('Her printer vi en simpel liste')
print(a)
print('\n')

#Lists are ordered
print('Lists er ordered vi sammenligner 2 lister')
b = ['baz', 'qux', 'bar', 'foo']

#burde returnere false
print(a == b)

#burde returnere true
b = ['foo', 'bar', 'baz', 'qux']
print('liste b er ændret til at være ens med liste a, burde nu returnere true')
print(a == b)
print('\n')

#Lists kan tilgås via index
print('Tilgå en liste via index nummer')
print(a[1])
print(a[-3])
print('\n')


#Man kan slice en list
a = [0,'et', 'to', 3, 'fire', 'fem', 6]
print('Her slicer vi en liste')
print(a)
print(a[1:4])
print(a[-5:-2])
print('\n')

#Lister kan være nested.
print('Nested liste')
x = ['a', ['bb', ['ccc', 'ddd'], 'ee', 'ff'], 'g', ['hh', 'ii'], 'j']
print(x)
print('printer index 0, 1 og 2')
print(x[0])
print(x[1])
print(x[2])
print('printer subliste x[1][0] og x[1][1]')
print(x[1][0])
print(x[1][1])
print('printer subliste x[1][1][0]')
print(x[1][1][0])
print('\n')

