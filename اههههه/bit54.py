def min_flips(a):
    r=[]
for i in range(1,len(a)):
    if a[i]!=a[i-1]:
        if a[i]!=a[0]: s=i
    else: r.append((s,i-1))
    if a and a[-1]!=a[0]: r.append((s,len(a)-1))
    return r

n=int(input())
a=list(map(int,input().split()))
for s,e in min_flips(a):
    print(f"From {s} to {e}")