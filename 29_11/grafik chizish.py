import numpy as np
import matplotlib.pyplot as plt
import math
s=input()
s=s.replace('^','**')
y=[]
z=[]
a,b = map(int,input("a va b").split())
n=int(input("Qadamlar: "))
h=(b-a)/n
for x in range(n+1):
    B = {
        "x": a+x*h,
        "sin": math.sin,
        "cos": math.cos,
        "tan": math.tan,
        "log": math.log,
        "sqrt": math.sqrt,
        "pi": math.pi,
        "e": math.e
    }
    z = z + [a+x*h]
    y = y+[eval(s,B)]
# x o'zgaruvchini oralig'ini kiritish
# grafikni hosil qilish
plt.plot(z, y, label="y = e^x", color="blue",linewidth=2)
# koordinata o'qlarini qo'shish
plt.axhline(0, color="black", linewidth=2)
plt.axvline(0, color="black", linewidth=2)
# izohlar va to'r
plt.xlabel("x")
plt.ylabel("y")
plt.title("Funksiya grafigi y = e^x va f=x^2")
plt.legend()
plt.grid(True)
# ko'rsatish
plt.show()
