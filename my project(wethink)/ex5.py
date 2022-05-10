try:
    number = int(input('Input number: '))
    if number < 0:
        print('this number is negative')
    elif number > 0:
        print('this number is positive')
    else:
        print('this number is 0')
except:
    print('Error, numeric value required')
