#write a python program to read size of list as input from the user and take the list elements as input from the user and find the 
#length of the list, the max element or number present in the list and similarly, 
#minimum element summation of elements of a list and print the sorted list in ascending order
num = int(input())
list1 = []
for i in range(num):
    temp = int(input())
    list1.append(temp)
print(list1)
print(len(list1))
print(max(list1))
print(min(list1))
print(sum(list1))
print(sorted(list1))