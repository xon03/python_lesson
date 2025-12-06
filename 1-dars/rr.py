def bol(n):
    s=0
    for i in range(1,n//2+2):
        if n%i==0:
            s=s+i
    if s==n:
        return True
    else:
        return False
n=int(input())
x=2
A=[]
while True:
    if bol(x):
        A.append(x)
    x=x+2
    if len(A)==n:
        break
print(A[-1])