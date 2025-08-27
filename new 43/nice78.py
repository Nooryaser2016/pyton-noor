number = int(input("enter ur number  "))
ori_num = number
reve_number = 0

while number > 0:
    digit = number % 10
    reve_number = reve_number * 10 + digit
    number //=10

if ori_num == reve_number:
    print(f"{ori_num} is a palindrome")
else:
    print(f"{ori_num} is not a palindrome")