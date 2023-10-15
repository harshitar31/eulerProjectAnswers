#euler 4 (largest palindrome made from the product of two 3-digit numbers)

number=[]
for i in range(100,1000):
    for j in range(100,1000):
        product=i*j
        f=str(product)
        r=f[::-1]
        if f==r:    #the last number does not have to be the largest
            number+=[product]
print(max(number))

