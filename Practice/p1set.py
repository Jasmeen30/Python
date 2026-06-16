set1={"apple","banana","cherry"}
set2 ={"pineapple", "mango", "papaya"}

print(set1)
print(type(set1))
print(len(set2))

set1.add("orange")
print(set1)

set1.update(set2)
print(set1)

set1.remove("banana")   #set1.discard("banana")
print(set1)

x = set1.pop()
print(x)
print(set1)

set1.clear()
#print(set1)

del set1
#print(set1)
