n=input()
b=''
c=n[::-1]
for i in range(len(n)-1,-1,-1):
    b=b+n[i]
if n==b:
    print("Ha")
else:
    print("Yo'q")
# input 12321, 89099
# output Ha, Yo'q