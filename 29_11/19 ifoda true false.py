s=input()
x=s.find('=')
a=s[:x]
b=s[x+1:]
if eval(a)==eval(b):
    print("To'g'ri")
else:
    print("Noto'g'ri")