
def maxProduct(arr):
    arr.sort()
    length = len(arr)
    return arr[length-3] * arr[length-2] * arr[length-1]

arr = [1,2,3,4,5]
print(maxProduct(arr))