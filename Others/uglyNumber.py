def maxDivide(a ,b):
    while a % b ==0:
        a = a / b
    return a 

def isUgly(n):
    n = maxDivide(n,2)
    n = maxDivide(n,3)
    n = maxDivide(n,5)
    if n ==1:
        return 1
    else:
        return 0

def uglyNum(n):
    i = 0
    count = 1

    while count<n:
        i+=1
        if isUgly(i):
            count+=1
    #return the index of n on the ugly number sequence            
    return i

n=150
print(uglyNum(n))