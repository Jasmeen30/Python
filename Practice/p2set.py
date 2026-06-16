set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

set4 = set1 | set2
print(set4)

set1.update(set2)
print(set1)

#intersection
set5 = set1.intersection(set2)
print(set5)

set6 = set1 & set2
print(set6)


#difference
set7 = set1.difference(set2)
print(set7)

set8 = set1 - set2
print(set8)

set1.difference_update(set2)
print(set1)