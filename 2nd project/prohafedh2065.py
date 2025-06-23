number = int(input("Enter a number: "))
original = number
sum = 0


digits = len(str(number))


temp = number

while temp > 0:
    digit = temp % 10
    sum = sum + (digit ** digits) 
    temp = temp // 10


if sum == original:
    print("Yes, it's an Armstrong number!")
else:
    print("No, it's not an Armstrong number.")
