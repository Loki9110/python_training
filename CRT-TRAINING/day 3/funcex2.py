'''write a function to calculate sum of first and last digit of a number'''


def calc(n):
     c=n%10   # for extracting last digit 
     while (n>1):    #for extracting the first digit
          l=n
          n=n//10  
     print(l+c)

calc(931)
