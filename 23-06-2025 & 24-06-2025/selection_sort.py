def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        mid_index = i
        for j in range(i+1,n):
            if arr[j]<arr[mid_index]:
                mid_index = j
        arr[i],arr[mid_index] = arr[mid_index],arr[i]
        print(arr)
selection_sort([5,4,3,2,1])

'''

'''