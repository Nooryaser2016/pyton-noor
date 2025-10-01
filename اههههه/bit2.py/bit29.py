def factorical(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorical(n -1)
res = factorical(6)
print(res)