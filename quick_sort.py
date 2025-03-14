def partition(arr, low, high):
    pivot = arr[high]   # Choosing last element as pivot
    i = low - 1         # Pointer for smaller element

    for j in range(low, high): 
        if arr[j] <= pivot:  # If current element is smaller than or equal to pivot
            i += 1           # Move index forward
            arr[i], arr[j] = arr[j], arr[i]  
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1] 
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        # Partition the array
        pi = partition(arr, low, high)  
        # Recursively apply quick_sort to left and right subarrays
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

arr = [7, 3, 8, 5, 9, 4]
quick_sort(arr, 0, len(arr) - 1)
print(arr)  
