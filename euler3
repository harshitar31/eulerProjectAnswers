#euler 3 (largest prime factor of the number 600851475143)

prime=True
number=600851475143
j=2
primeFactors=[]
for factor in range(2,number):
    if number%factor==0:
        while j<factor:
            if factor%j==0:
                prime=False
                break
            j+=1
        if prime:
            primeFactors+=[factor]
        j=2
        prime=True
print(primeFactors[-1])
