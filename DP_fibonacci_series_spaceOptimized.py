def fibo(n):

    if n<=0:
        return n
    if n==1:
        return [0]
    
    series=[0,1]
    a,b=0,1

    for i in range(2,n+1):
        c=a+b
        series.append(c)
        a=b
        b=c
    return series

n=int(input("Enter n:"))
print("Fibonacci Series:",fibo(n))
    
