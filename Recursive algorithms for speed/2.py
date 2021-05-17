
def findMissing(arr):
    arr.sort()
    for i in range(0,len(arr)):
        if i != arr[i]:
            return i
    return None

arr = [0,1,2,3,4,5,7]
print(findMissing(arr))