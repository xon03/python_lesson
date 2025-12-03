n=int(input())
s=[]
for i in range(1,n+1):
    if n%i==0:
        s.append(i)
print(s)
# input: 120
# output: [1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 20, 24, 30, 40, 60, 120]