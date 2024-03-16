#write a program to accept one single subject marks and chek if the marks are greateer than 35 he cheated ,if marks are equal to 35 he passed and marks less than 35 he failed

marks=int(input("enter your marks:"))

if marks>35:
    print("he cheated in the exam")
elif marks==35:
    print("he passed the exam")
else:
    print("he failed the exam")