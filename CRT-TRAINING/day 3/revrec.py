'''write a recursive program to print the digits of number in rev order'''

def r(n):
    if n==0:
        return  #we use this ro stop the exec
    else:
        d=n%10
        print(d)
        return  r(n//10)
print(r(12345))
    
