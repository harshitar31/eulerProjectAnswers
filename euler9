#euler 9 (There exists exactly one Pythagorean triplet for which a+b+c=1000, find a*b*c)

end=1000 
for a in range(1,end):
    for b in range(2,end):
        if b>a:
            for c in range(3,end):
                if c>b:
                    if a+b+c==1000:
                        if (a**2 + b**2)==c**2:
                            print(a*b*c)
                            end=0
