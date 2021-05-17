n= 7

def triangularNumber(n):
    
    #base case
    if n ==1: return 1
    return n + triangularNumber(n-1)

print(triangularNumber(n))