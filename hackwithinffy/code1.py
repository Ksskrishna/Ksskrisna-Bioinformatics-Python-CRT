'''
1. EASY
 You’re given an array A of n integers and q queries.
 Each query can be one of the following two types:
 • Type 1 Query: (1, l, r) - Replace A[i] with 
(i-l+1)*A[l] for each index i, where l <= i <= r.
 • Type 2 Query: (2, l, r) - Calculate the sum of the 
elements in A from index l to index r.
 Find the sum of answers to all type 2 queries. Since 
answer can be large, return it modulo 109+7.
'''
mod = 10**9 + 7
size = int(input("enter number of elements in list: "))
total_sum = 0

list = []
for i in range(size):
    temp = int(input("enter elements in list: "))
    list.append(temp)
print(list)

query = int(input("enter number of queries: "))
for i in range(query):
    parts = input().split()
    t = int(parts[0])
    l = int(parts[1])
    r = int(parts[2])
    if t == 1:
        for i in range(l,r+1):
            list[i] = (i-l+1)*list[l]
    elif t == 2:
        sum = 0
        for i in range(l,r+1):
            sum += list[i]
        total_sum = (total_sum+sum) % mod
print(total_sum)