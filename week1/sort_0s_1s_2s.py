def sortnums(arr):
    low = 0
    mid = 0
    high = len(arr) - 1
    while mid <= high:
        if arr[mid] == 0:
            arr[low],arr[mid] = arr[mid], arr[low]
            mid = mid + 1
            low = low + 1
        elif arr[mid] == 1:
            mid = mid +1 
        elif arr[mid] == 2:
            arr[mid],arr[high] = arr[high], arr[mid]
            high = high-1
            mid = mid + 1
    print(arr)
sortnums([1,1,1,1,0,0,0,0,2,2,2])

