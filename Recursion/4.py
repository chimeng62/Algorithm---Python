s= "abcdefghijklmnopqrstuvwxyz"

def findX(s):    
    #base case
    if s[0] == 'x': return 0
    return 1 + findX(s[1:len(s)])

print(findX(s))