#code that lets a user guess a random numbers between 0 and 10
import random

print("i'm thinking of a number between 1 and 10")
#handle exeception in case user enter wrong data type or leave blank
try:
    number = random.randint(0,10)
    guess = 0
    guess_count = 1
    
    #keep asking till user guess is the same as random number
    while guess != number:
        guess = int(input('take a guess: '))
        
        #compare user guess and number, give feedback
        if guess == number:
            print("Great job, you've guessed my number in "+str(guess_count)+' guesses!')
        elif guess < number:
            print('your guess is too low')
        else:
            print('your guess is too high')
        #encrement count for every iteration
        guess_count += 1
        
except:
    #print message in case of user error
    print('Error, number required')
