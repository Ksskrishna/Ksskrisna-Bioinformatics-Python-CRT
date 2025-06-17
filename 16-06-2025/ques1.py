'''
write a python program to write a lambda function which prints good students if branch is bioinfromatics else bad students
'''
#wrire a python program to prints good students if branch is bioinformatics else bad students
dep=lambda branch:print("good students") if branch=="bioinformatics" else print("bad students")
branch=input("enter branch:")
dep(branch)