def maxSubArraySum(a,a_size):
    max = -99999999999
    cmax = 0
    for i in range(0, a_size):
        cmax = cmax + a[i]
        if (max < cmax):
            max = cmax
        if cmax < 0:
            cmax = 0
    return max
a = [12,34,-32,3,-1,-1,13,-9,10]
print(maxSubArraySum(a,len(a)))
