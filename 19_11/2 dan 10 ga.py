n=input()
x=len(n)
s=0
for i in range(x):
    s+=int(n[i])*2**(x-i-1)
print(s)
# input: 10001001
# output: 137