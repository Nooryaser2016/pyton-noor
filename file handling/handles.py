h1 = open("file87.txt")
print(h1.read())

h1.close()

k1 = open("file87.txt","w")
k1.write("Codingal it has many good classes!")

k1.close()

k2 = open("file87.txt","a")
k2.write(" Codingal has many good projects!")
