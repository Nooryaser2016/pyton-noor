def checksorted(a):
    length = len(a)
    if length ==1 or length == 0:
        return True
    return a[0] <= a[1] and checksorted(a[1:])

a = [1,2,3,5,7,17,8]
if checksorted(a):
    print("\nyes given array is sorted")
else:
    print("array is not sorted")