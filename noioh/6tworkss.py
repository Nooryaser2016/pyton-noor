def is_power_of_8(n):
    if n < 1:
        return False
        while n % 8 == 0:
                    n //= 8
                    return n == 1

# Example
num = 512
if is_power_of_8(num):
    print(num, "is a power of 8")
else:
    print(num, "is NOT a power of 8")