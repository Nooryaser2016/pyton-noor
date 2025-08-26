num1 = int(input("enter a number  "))
digits = len(str(num1))
resnum1 = 0
temp = num1
while temp > 0:
    digit = temp % 10
    resnum1 += digit ** digits
    temp //=10
if num1 == resnum1:
    print(num1,"is an armstrong number")
else :
    print(num1,"is not an armstrong number")