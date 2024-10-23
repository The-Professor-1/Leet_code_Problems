n = 10

def fib(n):
    if n == 1 or n == 2:
        return 1
    lis = [None] * (n+1)
    lis[1] = 1
    lis[2] = 2
    for i in range(3,n+1):
        lis[i] = lis[i-1] + lis[i-2]
    return lis[n]
print(fib(350))