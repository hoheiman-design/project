import math

# Build Max-Heap
def build_max_heap(arr):
    n = len(arr)
    # max_heapify
    
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, n, i)

# Max-Heapify
def max_heapify(arr, n, i):
    largest = i        
    l = 2 * i + 1      
    r = 2 * i + 2      

    
    if l < n and arr[l] > arr[largest]:
        largest = l

    if r < n and arr[r] > arr[largest]:
        largest = r

    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  
        max_heapify(arr, n, largest)

#Heap Sort
def heap_sort(arr):
    n = len(arr)

    # 1
    build_max_heap(arr)

    # 2
    for i in range(n - 1, 0, -1):
    
        arr[0], arr[i] = arr[i], arr[0]
        
 
        max_heapify(arr, i, 0)
        
    return arr

# test
if __name__ == "__main__":
    test_arr = [12, 11, 13, 5, 6, 7]
    print(f"old: {test_arr}")
    sorted_arr = heap_sort(test_arr)
    print(f"new: {sorted_arr}")