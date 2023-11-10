#euler 10 (Sum of all the primes below two million)

psum=0
prime=True
for i in range(2,21):
    for j in range(2,(i//2)+1):
        if i%j==0:
            prime=False
            break
    if prime:
        psum+=i
        print(i)
    prime=True
print(psum)
