def sum(n):
    s=0
    for i in n:
        s=s+int(i)
    return s
def omadli(n):
    while len(n) > 1:
        n = str(sum(n))
    return n
s=input()
z=False
for i in range(1, len(s)):
    x=s[:i]
    y=s[i:]
    if omadli(x) == omadli(y):
        z=True
        break
if z:
    print("YES")
else:
    print("NO")
