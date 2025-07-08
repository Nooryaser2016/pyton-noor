t1 = ("hello",54,95.5)
print(t1[2])

my_set = {1,2,2,2,3,4,5,6,7,7,7,8,9,10}

print(my_set)

my_set.add(11)
print(my_set)



my_set2 = {2,3,15,11,45,78,99}
print(my_set2.intersection(my_set))
print(my_set2.union(my_set))
print(my_set2.symmetric_difference(my_set))