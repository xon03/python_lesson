a,b=map(int,input().split())
c,d=map(int,input().split())
e,f=map(int,input().split())
g,h=map(int,input().split())
if a+c+e+g>b+d+f+h:
    print('1')
elif a+c+e+g<b+d+f+h:
    print('2')
else:
    print('DRAW')