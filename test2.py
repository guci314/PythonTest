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

#%%
s='ppppppppppp'
print(s)
#%%
class X:
    def f(self):
        print('dfdf')
x=X()
x.f()

#%%
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
iris = load_iris()

x_index = 2
y_index = 1

# this formatter will label the colorbar with the correct target names
formatter = plt.FuncFormatter(lambda i, *args: iris.target_names[int(i)])

plt.scatter(iris.data[:, x_index], iris.data[:, y_index],
            c=iris.target, cmap=plt.cm.get_cmap('RdYlBu', 3))
plt.colorbar(ticks=[0, 1, 2], format=formatter)
plt.clim(-0.5, 2.5)
plt.xlabel(iris.feature_names[x_index])
plt.ylabel(iris.feature_names[y_index]);

#%%
x=np.arange(10)
x+=10
y=np.sum(x)
y=np.mean(x)
print(y)
#%%
