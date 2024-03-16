'''write a recursive function to sum of digits'''

def sumrec(n):
    
    if n==0:
        return 0  #basecase where 0=0 
    
    return n%10 + sumrec(n//10)

print(sumrec(12345))
    