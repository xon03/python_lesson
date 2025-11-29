import math
s=input()
x=2
s=s.replace('^','**')
B ={
    "x": x,
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "log": math.log,
    "sqrt": math.sqrt,
    "pi": math.pi,
    "e": math.e
}
print(eval(s,B))