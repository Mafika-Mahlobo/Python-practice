user_name = ''
password = ''
while user_name == '' or password == '':
    user_name = input('enter your username: ')
    password = input('enter your password: ')
    if user_name == '' or password == '':
        print('both values are required!')

print(' ')
print('Hello '+user_name)

if password == 'LearningPythonIsFun':
    print('Access Granted')
else:
    print('Access Denied')
