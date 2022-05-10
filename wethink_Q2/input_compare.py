user_numbers = []      
try:
    for count in range(1,3,1):
        if count > 1:
            user_numbers.append(int(input('enter '+str(count)+'nd number: ')))
        else:
            user_numbers.append(int(input('enter '+str(count)+'st number: ')))
            
    if user_numbers[0] > user_numbers[1]:
        print(str(user_numbers[0])+' is the larger number')
    elif user_numbers[0] < user_numbers[1]:
        print(str(user_numbers[1])+' is the larger number')
    else:
        print('the numbers are equal')
except:
    print('an error occuured, you should provide a numeric value')
    
        
            

    
        
    
        
