import time
n=int(input("n faktorialni kiriting: "))
s=0
a=time.time()
while n>=5:
    s=s+n//5
    n=n//5
b=time.time()
print(s)
print(b-a)
# input: 300
# output: 74, 4.291534423828125e-06
# input: 20
# output: 4, 1.9073486328125e-06