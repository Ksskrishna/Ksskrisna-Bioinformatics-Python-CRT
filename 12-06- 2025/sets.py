set = {10,20,30,25,40,31,34}
print(type(set))
set.add(50)
print(set)
print(50 in set)

set_2 = {60,45,80,100}
set.update(set_2)
print(set)

#remove
set.remove(50)
print(set)
#using discard
set.discard(200)
print(set)
#pop
set.pop()
print(set)

# we can use | or & 
print(set & set_2)

#using intersection 
set.intersection(set_2)
print(set)

set.union(set_2)
print(set)