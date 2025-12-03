n=int(input())
s=[]
while n:
    s.append(str(n%2))
    n=n//2
s.reverse()
print("".join(s))
# input: 137
# output: 10001001