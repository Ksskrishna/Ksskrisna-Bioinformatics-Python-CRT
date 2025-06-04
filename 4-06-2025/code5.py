cartoon = ['Doraemon','shinchan','ben10','tom','high school']
print(cartoon)
print("after appending")
cartoon.append('rool No.21')
print(cartoon)
print("to add at specific index use insert")
cartoon.insert(1,"Krishna") #used to insert at specific index
print(cartoon)
cartoon.pop() #removes last element
print(cartoon)
#to remove at specific element
cartoon.pop(0)
print(cartoon)
#for removing element based on element but not through index you can use remove()
cartoon.remove("ben10")
print(cartoon)
#using index method
cartoon.index("tom")
print(cartoon)
#to reverse 
numbers = [5,555,55,8,5]
print(numbers)
numbers.reverse()
print(numbers)