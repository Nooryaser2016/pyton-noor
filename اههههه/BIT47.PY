def calprofits(arr, arr_size):

    pro = 0

    for i in range(1, arr_size):
     # start from 1, not 0

        if arr[i] > arr[i-1]:

         pro += arr[i] - arr[i-1]

    return pro
prices = [678,355,612,344,59,222,456]
profit = calprofits(prices, len(prices))
print("Max profit :",profit)



    