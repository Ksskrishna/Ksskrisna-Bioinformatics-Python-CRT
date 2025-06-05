#write a python program to remove duplicate values from the list

list1 = [20,208,41,4115,54,15,41,20]
unique_list = []
for i in list1:
    if i not in unique_list:
        unique_list.append(i)
print(unique_list)