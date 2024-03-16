'''write a recrusion program for armstrong number'''

def c(n):
    if n==0:
        return 0
    return 1+ c(n//10)
def  arms(n):
    if n==0:
        return 0
    return ((n%10)**cou) + arms(n//10)

cou=c(153)

print(arms(153))
    
