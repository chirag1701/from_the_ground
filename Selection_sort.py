# SELECTION SORT : selecting minimum and swapping
def minima(arr):
    min_index = 0
    for i in range(1,len(arr)):
        if arr[i]<arr[min_index]:
            min_index = i
    return min_index
def swap(i,j,arr):
    n1 = arr[i]
    arr[i] = arr[j]
    arr[j] = n1
    return arr
def sel_sort(arr):
    for i in range(0,len(arr)-1):
        min = minima(arr[i:]) + i 
        arr = swap(min,i,arr)
    return arr
arr = eval(input())    
print(sel_sort(arr))  
