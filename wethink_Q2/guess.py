import random
try:
    guess = int(input('guess a number between 1 and 10: '))
    if guess == random.randint(1,10):
        print('Correct')
    elif guess > 10 or guess < 1:
        print('answer shuld be between 1 and 10')
    else:
        print('Wrong answer')
except:
    print('you sould enter a numeric value')
