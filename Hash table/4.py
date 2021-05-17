text = 'minimum'

def findFirstDup(text):
    dictionary = {}

    for i in text:
        if dictionary.get(i):
            dictionary[i] +=1; 
        else:
            dictionary[i] = 1
    for key,val in dictionary.items():
        if val == 1:
            return key
print(findFirstDup(text))