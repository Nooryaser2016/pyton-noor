def  arrayMean(arr,arr_size):
    total_sum = 0 
    for i in range(0,arr_size):
        total_sum += arr[1]
    return float(total_sum/arr_size)

arr = [1,4,5,2,8,5,2,6,8]
arr_size = len(arr)

print("mean =", arrayMean(arr,arr_size))
arr.append(12)
print(arr)
arr.insert(5,16)
print(arr)
arr.pop()
print(arr)
    