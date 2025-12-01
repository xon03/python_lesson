n=int(input())
a=[1,1]
for i in range(2,n):
    a.append(a[-1]+a[-2])
print(a)
# input 10
# output [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]