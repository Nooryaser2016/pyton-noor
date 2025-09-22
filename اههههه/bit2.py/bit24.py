def reverseBits(num):

    binary = bin(num)[2:]

    reversed_binary = binary[::-1]

    return int(reversed_binary, 2)

num1 = 12
print("Original:", num1, "Reversed:", reverseBits(num1))

num2 = 11
print("Original:", num2, "Reversed:", reverseBits(num2))