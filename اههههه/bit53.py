def longest_odd_even_subarray(arr):
    if not arr:
        return 0

best = 1
curr = 1

    for i in range(1, len(arr)):
        if (arr[i] % 2) != (arr[i - 1] % 2): # parity alternates
    curr += 1
    else:
        curr = 1
    best = max(best, curr)

    return best


# --------- input/output style ----------
n = int(input().strip())
arr = list(map(int, input().split()))
print(longest_odd_even_subarray(arr))