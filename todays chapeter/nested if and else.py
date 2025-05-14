m=input("enter yes or no")
a=int(input("enter your attendence"))
if m =='y':
    print('you can give the exam')
else:
    if a > 75:
    
        print('you cant give the exam')
    else:
        print('you are not aligibal for the exam')