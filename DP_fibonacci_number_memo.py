def fibo(n,memo=None):

    if memo==None:
       memo={}

    if n in memo:
        return memo[n]

    if n<=1:
        return n 

    memo[n]=fibo(n-1,memo)+fibo(n-2,memo)
    return memo[n] 

n=int(input("Enter n:"))
print("Fibonacci Number:",fibo(n))