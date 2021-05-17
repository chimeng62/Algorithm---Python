#N2 complexity solution
def maxValue1(arr):
    isMax = False
    for i in arr:
        isMax = True
        for j in arr:
            if j>i:
                isMax = False
        if isMax:
            return i
            

#N complexity solution
def maxValue2(arr):
    currentMax=arr[0]
    
    for i in arr:
        if i>currentMax:
            currentMax=i
    return currentMax

#NLogN complexity solution
def maxValue3(arr):
    arr.sort()
    return arr[len(arr)-1]

arr = [3,5,6,9,2,1]
print(maxValue1(arr))
#print(maxValue2(arr))
#print(maxValue3(arr))