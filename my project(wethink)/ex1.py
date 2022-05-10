try:
    from datetime import datetime
    name = ''
    age = ''
    while name == '' or age == '':
        name = input('what is your name?: ')
        age = input('how old are you?: ')
        if name == '' or age == '':
            print('both values are required!')
            
    years_remaining = 100 - int(age)
    year_of_turning100 = datetime.today().year + years_remaining
    print(' ')
    print(str(name)+' you will turn 100 years old in '+str(year_of_turning100))
except:
    print('error, a numeric value is required for age!')
