n=int(input('n='))
T=[2]
for i in range(3,n*n+1,2):
    for j in T:
        if i%j==0:
            break
    else:
        T.append(i)
        if len(T)==n:
            break
print(T)
# input n=13
# output [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]