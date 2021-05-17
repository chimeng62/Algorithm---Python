
def fi(n, memo):
    
    if memo[n] is not None:
        return memo[n]
    #return 1 if n is 1 or 2
    if n ==1 or n == 2:
        return 1
    else:
        memo[n] = fi(n-1, memo) + fi(n-2, memo)
        return memo[n]
#n=533
#memo = [None]*(n+1)
#print(fi(n))

def fi_bottom_up(n):
    
    #return 1 if n is 1 or 2
    if n ==1 or n == 2:
        return 1
    arr = [None]*(n+1)
    arr[1] = 1
    arr[2] = 1

    #loop through array & calculate the value for the next index

    #i starts from 3
    for i in range(3,n+1):
        arr[i] = arr[i-1] + arr[i-2]
    return arr[n]

n=500
memo = [None]*(n+1)
print(fi_bottom_up(n))
