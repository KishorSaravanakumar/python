def fibonacci(n):
    a,b=0,1
    print("The fibonacci series of",n,"is:")
    print(a,b,end=" ")
    for i in range(2,n):
        c=a+b
        print(c,end=" ")
        a=b
        b=c
    print("\n")
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
n=int(input("Enter a number:"))
fibonacci(n)
print("The factorial number of",n,"is",factorial(n))
