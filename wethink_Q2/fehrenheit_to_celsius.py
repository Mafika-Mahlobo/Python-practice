try:
    fehrenheit = input('provide a temperature in fehrenheit: ')
    celsius = ((int(fehrenheit)-32)*(5/9))
    print(' ')
    print(str(fehrenheit)+' degrees ferenheits is equal to '+str(celsius)+' degrees celsius')
except:
    print('numeric value reqired')
