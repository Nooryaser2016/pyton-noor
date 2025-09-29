def longest_ones(n):
# Convert number to binary string (bin returns string starting with '0b')
    binary = bin(n)[2:]
# Split by '0' and take the longest sequence of '1's
    return max(len(seq) for seq in binary.split('0'))

# Example
num = 56
print("Binary:", bin(num)[2:])
print("Longest consecutive 1's:", longest_ones(num))