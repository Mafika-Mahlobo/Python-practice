try:
    hour = int(input('enter an hour value to convert it to seconds: '))
    seconds = hour*3600
    print(' ')
    print(str(hour)+' hours is equal to '+str(seconds)+' seconds')
except:
    print('numeric value required')

