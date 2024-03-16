'''design a login function  which accepts the user only when the username annd password are same and dispaly a message login succesful otherwise it keeps asking the user to enter the credentials'''


def credentials():
    
    while(69):  #infinite loop you can give any number of ur choice 
        us=int(input("enter the username:"))
        pas=int(input("enter the password:"))
        if us==pas:
            print("the credentials are correct")
            break
        else:
            print("not correct")
            print("enter the credentials again bruv")  #add credentials() in the else for the recursion 

credentials()
