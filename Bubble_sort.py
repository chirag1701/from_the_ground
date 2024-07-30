# BUBBLE SORT - pushes the max to the last by adjacent swapping 
arr = [24, 32, 22, 46, 6, 9, 21]
def push_max(arr, end):
    for i in range(0, end-1):
        if arr[i]>arr[i+1]:
           n1 = arr[i]
           arr[i] = arr[i+1]
           arr[i+1] = n1
    return arr
def bubble_sort(arr):
    for i in range(0,len(arr)):
        push_max(arr, len(arr)-i)
    return arr 
print(bubble_sort(arr))      
