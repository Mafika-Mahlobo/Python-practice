#function that takes a number and compute return value based on whether it's odd or even

def collatz(number):
    #check if number is odd or even
    if number%2 == 0:
        return number//2
    else:
        return 3*number+1

"""
run the prorgam with F5 then call the function on python shell/terminal e.g
>>>callatz(5)
   
 """
