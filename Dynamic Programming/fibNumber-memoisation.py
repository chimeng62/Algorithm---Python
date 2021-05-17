
def fib(n,memo):
    #base case
    if n == 0 or n == 1:
        return n
    if not memo.get(n):
        memo[n] = fib(n-1,memo) + fib(n-2,memo)
    return memo[n]

n=10
#dictionary
memo = {}
print(fib(n,memo))