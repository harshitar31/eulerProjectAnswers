# python code

c=1
mc=0
mn=0
for i in range(1,1000000):
    num=i
    while num!=1:
        c+=1
        if num%2==0:
            num/=2
        else:
            num=3*num + 1
    if c>mc:
        mc=c
        mn=i
        print(mc,mn)
    c=1
print(mc,mn)

// java code

public class collatzConjecture {
	public static void main (String[] args) {
		double c=1,mc=0,mn=0;
		for (int i=13; i<1000000; i++) {
			double num=i;
			while (num!=1) {
				c+=1;
				if (num%2==0) {
					num=num/2;
				}
				else {
					num= 3*num + 1;
				}
			}
			if (c>mc) {
				mc=c;
				mn=i;
			}
			c=1;
		}
		System.out.println(mc);
		System.out.println(mn);
	}
}
