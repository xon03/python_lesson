m1,m2,m3=map(int,input().split())
if min(m1,m2,m3)>=94 and max(m1,m2,m3)<=727:
    print(max(m1,m2,m3))
else:
    print('Error')