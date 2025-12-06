n=int(input('n='))
T=[2]
def isPrime_small(k):
    if k<2:return False
    for j in T:
        if j*j>k:break
        if k%j==0:return False
    return True
def lucas_lehmer(p):
    if p==2:return True
    M=(1<<p)-1
    s=4
    for _ in range(p-2):
        s=(s*s-2)%M
    return s==0
count=0
i=2
while count<n:
    if i==2 or isPrime_small(i):
        if lucas_lehmer(i):
            T.append(i)
            count+=1
    i+=1 if i==2 else 2
x=T[-1]
p=(2**(x-1))*((2**x)-1)
print(p)