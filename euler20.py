# https://projecteuler.net/problem=20

def factorial(n):
    if n==1:
        return 1
    return n * factorial(n-1)

num = str(factorial(100))
total=0
for i in num:
    total+=int(i)
    
print(total)
