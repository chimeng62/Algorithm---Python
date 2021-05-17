def bubbleSort(arr):
    n= len(arr)
    for i in range(0,n):
        for j in range(1,n):
            if arr[j-1] > arr[j]:
                arr[j],arr[j-1] = arr[j-1],arr[j]
    return arr


arr= [5,2,3,1,4]

print(bubbleSort(arr))