'''
****
****
****
****
'''
n = int(input())
for i in range(n):
    for j in range(n):
        print("* ",end  = " ")
    print()
print("______________________")
for i in range(n,0,-1):
    for j in range(1,i+1):
        print("* ",end = " ")
    print()
print("________________________")
for i in range(1,n+1):
    for j in range(1,i+1):
        print("* ",end = " ")
    print()
print("______________________")
