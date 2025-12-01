# read size of array
n = int(input())

# read numbers separated by spaces
arr = list(map(int, input().split()))

# reverse in place
left, right = 0, n - 1
while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1

# print reversed array
print(" ".join(map(str, arr)))