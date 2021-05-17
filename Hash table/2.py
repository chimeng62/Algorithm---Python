arr1 =  ["a", "b", "b","c", "d", "c", "e", "f"]

def findFirstDup(r1):
    dictionary = {}

    for i in r1:
        if(dictionary.get(i)):
            return i
        else:
            dictionary[i] = True

print(findFirstDup(arr1))