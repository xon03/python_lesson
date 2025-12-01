n=list(map(int,input().split()))
a=0
for i in n:
    if i%2==0:
        a=a+1
b=len(n)-a
if a>b:
    print("juft sonlar")
elif a<b:
    print("toq sonlar")
else:
    print("teng")
# input 2 4 6 7
# output juft sonlar