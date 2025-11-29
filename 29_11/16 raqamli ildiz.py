n=input()
def sum(n):
    s=0
    for i in n:
        s=s+int(i)
    return s
while len(n)>1:
    n=str(sum(n))
print(n)
