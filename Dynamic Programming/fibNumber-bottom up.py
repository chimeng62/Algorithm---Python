
def fib(n):
    #start with the first 2 numbers of the series
    a=0
    b=1

    for i in range(1,n):
        temp = a
        a=b
        b=temp+a
    return b

n=10

print(fib(n))