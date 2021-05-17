arr= [1,2,3,4,5,6]
newArr = []
def evenOnly(arr):
    
    #base case
    if len(arr) == 0:
        return newArr

    if arr[0] % 2 == 0:
        newArr.append(arr[0])
    return evenOnly(arr[1:len(arr)])

print(evenOnly(arr))