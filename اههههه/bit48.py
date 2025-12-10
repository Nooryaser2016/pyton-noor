def getmaxlen(a, a_size):

    c = 0

    maxones = 0


    for i in range(0, a_size):

        if a[i] == 1:

            c = c + 1

        else:
    
            c = 0

            maxones = max(maxones, c)

    return maxones

a = [1,1,0,1,0,1,1,1,1]

a_size = len(a)

print("Max 1's:", getmaxlen(a, a_size))

