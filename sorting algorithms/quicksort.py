def partition(arr,left,right):
    #choose pivot
    pivot = arr[right]

    #pointer for greater element than pivot
    i = left -1

    #traverse through all elements
    #compare each with pivot
    for j in range(left,right):
        if arr[j] <= pivot:
            #if element smaller than pivot, swap it with the greater element pointed by i
            i +=1

            #swap element at i with j
            arr[i], arr[j] =arr[j], arr[i]
    #swap pivot element with the greater element pointed by i
    arr[i+1], arr[right] = arr[right], arr[i+1]

    #return the position from where partition is done
    return i + 1 

def quicksort(arr,left,right):
    if left<right:
        # find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(arr,left,right)

        #recusive call on the left of pivot
        quicksort(arr,left,pi-1)

        #recusive call on the left of pivot
        quicksort(arr,pi+1,right)




data = [8, 7, 2, 1, 0, 9, 6]
print("Unsorted Array")
print(data)

size = len(data)

quicksort(data, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(data)