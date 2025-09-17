def OddOccuring(arr):
  res = 0
  for element in arr:
    res = res ^ element
  return res
A1=[]
a = int(input("enter a array size  "))
while(a):
    num = int(input("enter a number "))
    A1.append(num)
    num-=1
print("oddoccurding number is",OddOccuring(A1))
