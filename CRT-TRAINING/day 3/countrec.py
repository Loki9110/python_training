'''write a recursive function to count the number of digits of a number'''

def dig(n):
    if n == 0:  #basecase
        return 0
    
    return  1+dig(n//10)

print(dig(123))


    