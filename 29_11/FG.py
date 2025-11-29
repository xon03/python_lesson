import math
import matplotlib.pyplot as plt
import numpy as np
def f(x):
    return (math.exp(x)-x*x);
a,b=map(int,list(input().split()))
n=20
x=[]
y=[]
h=(b-a)/n
for i in range(n):
    x=x+[a+i*h]
    y=y+[f(x[i])]
plt.plot(x,y)
plt.grid(True)
plt.show()



