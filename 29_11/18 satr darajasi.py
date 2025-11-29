s=input()
n=int(input())
if n>0:
    if len(s)*n>1023:
        n=1023//len(s)+1
    z=n*s
    print(z[:1023])
elif n==0:
    print(1)
else:
    x=len(s)%(-1*n)
    y=len(s)//(-1*n)
    l=s[:y]
    if x==0 and (-1)*n*l==s:
        print(l)
    else:
        print("NO SOLUTION")
