def ispowerOfTwo(x):
    if(x == 0):
        return False
    else:
        return (x & (x - 1)) == 0
    
n = int(input("enter a number :"))
if ispowerOfTwo(n):
    print("this is the power of two")
else:
    print("this is not a power of two")