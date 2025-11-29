n=input()
def sum(n):
    s=0
    for i in n:
        s=s+int(i)
    return s
x=0
while len(n)>1:
    n=str(sum(n))
    x=x+1
print(n)
print(x, "ta qadam")
