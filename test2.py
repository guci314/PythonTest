import numpy as np

def nptest():
    start = -1
    stop = 1
    x = np.linspace(start, stop, num=50)
    return x

aaa = nptest()

print(type(aaa))

def f(x:int)->int:
    return x+1

y=f(7)
print(y)


