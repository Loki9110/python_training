#write a function which takes  two parameters a and b typecaste the value of the seconfd argument into integer then multiply both the arguments and print the last digit og the result


def types(a,b):   #these are the parameters
    c=1
    b=int(b)
    c=a*b
    c%10
    print(c%10)


types(2,4)   #these are arguments
types(b=4,a=3)   #this is an example of keyword arguments

    # this is an example of positional arguments