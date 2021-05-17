arr= ['ab','c','def','aadd']

def charCount(array):
    #base case
    if len(array) == 0: return 0
    return charCount(array[1:len(array)]) + len(array[0])

print(charCount(arr))