def selectionSort(arr):
    minIndex = 0

    for i in range(0,len(arr)):
        minIndex = i
        for j in range(i+1,len(arr)):
            #if element smaller than current minimum
            if arr[j] < arr[minIndex]:
                minIndex = j
        #if no new minIndex, minIndex still = i
        if i != minIndex:
            arr[i],arr[minIndex] = arr[minIndex],arr[i]
    return arr


arr= [5,2,3,1,4]

print(selectionSort(arr))