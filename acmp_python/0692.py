n=int(input())
a=n
s=0
while n>1:
    n=n//2
    s=s+1
if 2**s==a:
    print('YES')
else:
    print('NO')