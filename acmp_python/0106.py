n=int(input())
s=0
g=0
for i in range(n):
    a=int(input())
    if a==0:
        s=s+1
    else:
        g=g+1
print(min(s,g))