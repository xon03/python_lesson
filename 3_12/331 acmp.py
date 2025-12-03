o=input()
s,m=map(int, input().split())
ao=int(o[:2])
bo=int(o[3:])
t2=(bo+m)//60
s1=str((ao+s+t2)%24)
s2=str((bo+m)%60)
if len(s1)==1:
    s1="0"+s1
if len(s2)==1:
    s2="0"+s2
r=s1+':'+s2
print(r)