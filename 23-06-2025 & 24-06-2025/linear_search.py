index = 0
def linear_Search(key,arr):
    for i in range(len(arr)):
        if arr[i]==key:
            return i
    return None
        
arr = [1,2,3,4,5,6]
key = 10
res = linear_Search(key,arr)
print(f"the element found at index: {res}")