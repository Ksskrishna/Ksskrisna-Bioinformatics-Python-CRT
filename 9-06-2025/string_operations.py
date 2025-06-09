'''
string operators - basic, Membership, Comparision
Basic - string Replication and String Concatenation
Membership - "in" and "NOt in"
Comparision operators - <,>, >=,<=,!=
'''
str = "Python"
print(f"Length of {str} is {len(str)}")
#accessing without index
for i in str:
    print(i,end = " ")
print()
#accessing with index
for i in range(len(str)):
    print(str[i],end = " ")


