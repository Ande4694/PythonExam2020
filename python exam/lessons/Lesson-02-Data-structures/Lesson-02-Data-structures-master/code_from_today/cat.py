import sys

def cat(filename):
    file_object = open(filename, 'r')
    
#    text = file_object.read()
#    print(text)

    #for line in file_object:
    #    print(line, end='')    

    lines = file_object.readlines()
    print(lines)

def main():
    cat(sys.argv[1])


if __name__ == "__main__":
    main()
