s=input()
x=s.find('=')
a=s[:x]
b=s[x+1:]
if eval(a)==eval(b):
    print("YES")
elif eval(a)!=eval(b):
    print("NO")
else:
    print("ERROR")