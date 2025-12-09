def missingNumber(arr, n):
    total_sum = n * (n + 1) // 2
    array_sum = sum(arr)
    return total_sum - array_sum

# Example
arr = [1, 2, 4, 5]
n = 5
print(missingNumber(arr, n)) # Output: 3