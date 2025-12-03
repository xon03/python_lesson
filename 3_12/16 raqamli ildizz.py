def ry(n):
    if n<10:
        return n
    else:
        return n%10+ry(n//10)
def ry2(n):
    if n<10:
        return n
    else:
        return ry2(ry(n))
n=int(input())
print(ry2(n))
# Input: 943, 42
# output: 7, 6