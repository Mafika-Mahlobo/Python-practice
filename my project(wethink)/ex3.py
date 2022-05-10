try:
    number1 = int(input('enter a number between 0 and 9: '))
    number2 = int(input('enter another number between 0 and 9: '))

    if number1 > 9 or number1 < 0 or number2 > 9 or number2 < 0:
        print('Error, the numbers are not within the range 0-9')
    else:
        numbers_sum = number1+number2
        if numbers_sum > 15:
            print(20)
        else:
            print('the sum is: '+str(numbers_sum)) 
except:
    print('Error, numeric values required!')
  

