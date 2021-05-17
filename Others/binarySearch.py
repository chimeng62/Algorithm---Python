def binarySearch(arr, target):
    index = -1
    left = 0 
    right = len(arr) -1

    while left <= right:
        #middle index
        mid = (left+right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid+1
        else:
            right = mid-1

    return index

 
arr= [1,2,3,4,5]

print(binarySearch(arr,4))