#euler 12 (Value of the first triangle number to have over five hundred divisors)

triangleNumber=0
i=1
factors=[]
while True:
    for j in range(1,i+1):
        triangleNumber+=j
        
    for fact in range(1,triangleNumber+1):
        if triangleNumber%fact==0:
            factors+=[fact]
            
    if len(factors)>500:
        print(triangleNumber)
        break
    i+=1
    triangleNumber=0
    factors=[]  
