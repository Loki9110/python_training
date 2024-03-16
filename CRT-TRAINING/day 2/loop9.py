for i in range(0,5):
    for s in range(0,5-i+1):
        print(" ",end=" ")
    for j in range(0,2*i+1):
        if(i==0 or i==4 or j==1 or j==2*i+1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()