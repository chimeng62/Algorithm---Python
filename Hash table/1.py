arr1 =  [1, 2, 3, 4, 5]
arr2 = [0, 2, 4, 6, 8] 

def findIntesection(r1,r2):
    result = []
    dictionary = {}
    for i in r1:
        dictionary[i] = True

    for j in r2:
        if(dictionary.get(j)):
            result.append(j)
    return result

print(findIntesection(arr1,arr2))