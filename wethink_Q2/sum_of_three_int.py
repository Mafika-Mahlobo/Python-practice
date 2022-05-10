try:
    numbers = []
    for count in range(1,4,1):
        numbers.append(int(input('enter number '+str(count)+': ')))

    if numbers[0] == numbers[1] or numbers[0] == numbers[2] or numbers[1] == numbers[2]:
        print(0)
    else:
        number_sum = numbers[0]+numbers[1]+numbers[2]
        print('the sum is: '+str(number_sum))
except:
    print('you should enter a numeric value')



    


    

     
