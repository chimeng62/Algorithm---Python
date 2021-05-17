text = 'the quick brown box jumps over a lazy dog'

def findMissingLetter(text):
    dictionary = {}
    al = "abcdefghijklmnopqrstuvwxyz"

    for i in text:
        dictionary[i] = True

    for j in al:
        if not dictionary.get(j):
            return j
print(findMissingLetter(text))