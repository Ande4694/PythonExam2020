from menu import plugins

while(True):
    
    i = input(f'Type: {list(plugins.keys())} : ')
    print(    plugins[i]()     )
    
