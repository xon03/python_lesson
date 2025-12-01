s=input()
# x=s.find('=')
# a=s[:x]
# list="+,-,*,/"
#
# b=s[x+1:]
# try:
#     if eval(a)==eval(b):
#         print("YES")
#     elif eval(a)!=eval(b):
#         print("NO")
#     else:
#         print("ERROR")
# except Exception:
#     print("ERROR")
amal='*,+,-,/'
alifbo='abcdefghijklmnopqrstuvwxyz'
u=False
for i in alifbo:
    if i in s:
        u=True
        break
t="="
if t not in s or " " in s or s[0]=="+" or u:
    print("ERROR")
else:
    x = s.find('=')
    a = s[:x]
    b = s[x + 1:]
    try:
        if eval(a)==eval(b):
            print("YES")
        elif eval(a)!=eval(b):
            print("NO")
        else:
            print("ERROR")
    except Exception:
        print("ERROR")