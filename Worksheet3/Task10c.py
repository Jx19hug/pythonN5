for count in range(1, 6):
    output = ''
    for things in range(5, 0, -1):
        if things == count:
            output = output + str(count) 
        else:
            output = output + '.'
    print(output) 

