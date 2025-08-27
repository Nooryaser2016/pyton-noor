numlar = int(input("Enter largest number  "))
numsmallest = int(input("Enter smallest number  "))

while(numsmallest):
    num_store = numsmallest
    numsmallest = numlar % numsmallest
    numlar = num_store

print("HCF IS  ",numlar)
