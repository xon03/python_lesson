import numpy as np
import matplotlib.pyplot as plt
import math
# x o'zgaruvchini oralig'ini kiritish
x = np.linspace(-2, 2, 100)  #  [-2; 2] jami 100 ta nuqta
y = np.exp(x)-x**2  # funksiya y(x) = e^x
# grafikni hosil qilish
plt.plot(x, y, label="y = e^x", color="blue",linewidth=2)
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
