n=list(map(int,input().split()))
for i in range(len(n)):
    for j in range(i+1,len(n)):
        if n[i]>n[j]:
            n[i],n[j]=n[j],n[i]
print(n)
# input 9 10 -23 200 18 1 9
# output [-23, 1, 9, 9, 10, 18, 200]