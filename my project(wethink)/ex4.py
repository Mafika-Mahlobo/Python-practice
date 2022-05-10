name = ''
while name == '':
    name = input('input name: ')
    if name == '':
        print('name required')
print('Hi '+name+'! lets play hangman..,.')
guess = input("guess the missing letter in 'fun_tion' : ").lower()
if guess == 'c':
    print('Good guess')
    print('the word was: function')
else:
    print('Incorrect')
    print('the word was: function')
