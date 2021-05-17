def insertionSort(arr):
    n= len(arr)
    for i in range(0,n):
        j = i
        current = arr[i]

        while j>0 and current < arr[j-1]:
            arr[j] = arr[j-1]
            j-=1
        
        arr[j] = current
    return arr


arr= [5,2,3,1,4]

print(insertionSort(arr))