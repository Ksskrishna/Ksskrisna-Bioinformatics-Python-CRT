size = int(input("enter the number of students: "))
students = []
for i in range(size):
    temp = input("enter student names: ")
    students.append(temp)
students[1],students[2]=students[2],students[1]
print(students)