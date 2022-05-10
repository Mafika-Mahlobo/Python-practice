try:
    values = []
    for count in range(1,4,1):
        values.append(input('enter value '+str(count)+': '))

    average = (int(values[0])+int(values[1])+int(values[2]))/3
    print(' ')
    print('the average is: '+str(average))
except:
    print('numeric value required')
