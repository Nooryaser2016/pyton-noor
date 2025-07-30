with open("andy7.txt" , "r") as k7:
    data = k7.readlines()
    for line in data:
        word = line.split()
        print(word)
k7.close()

f2 = open("k7.txt" , "x")
import os
os.remove("k7.txt")
os.rmdir("hafedh")