import math

# take two numbers from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# calculate LCM using GCD
lcm = (num1 * num2) // math.gcd(num1, num2)

print("LCM is:", lcm)