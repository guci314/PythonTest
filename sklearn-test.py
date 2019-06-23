#%%
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# use seaborn plotting defaults
import seaborn as sns; sns.set()
#%%
from sklearn.datasets import make_blobs
import matplotlib 

X, y = make_blobs(n_samples=300, centers=4,
                  random_state=0, cluster_std=1.0)
plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='rainbow');
plt.show()
#%%
from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(n_estimators=100, random_state=0,n_jobs=-1)
clf.fit(X,y)
y_predict=clf.predict(X)

plt.scatter(X[:, 0], X[:, 1], c=y, cmap='rainbow');
plt.figure()
plt.scatter(X[:, 0], X[:, 1], c=y_predict, cmap='rainbow');
plt.show()
#%%
from sympy import *

# 初始化
x = symbols('x')

# 表达式
expr1 = cos(x)

expr2 = exp(x**2)


# 求导
r1 = diff(expr1, x)
r2 = diff(expr2, x)


print("r1:", r1)
print("r2:", r2)

print("finished")

#%%
from sympy import *


# 初始化
x = symbols('x')

# 表达式
expr1 = sin(x)/x
expr2 = 1/x

# 求趋于某个值的极限
r1 = limit(expr1, x, 0)

# 正向趋进
r2 = limit(expr2, x, 0, '+')

# 负向趋进
r3 = limit(expr2, x, 0, '-')

print(r1)
print(r2)
print(r3)

#%%
x=np.linspace(0,1,10)
y=x**2
#%%
plt.plot(x,y)
plt.show()

#%%
from sklearn.datasets import load_digits
digits=load_digits()
digits.keys()
X=digits.data
y=digits.target

# set up the figure
fig = plt.figure(figsize=(6, 6))  # figure size in inches
fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)

# plot the digits: each image is 8x8 pixels
for i in range(64):
    ax = fig.add_subplot(8, 8, i + 1, xticks=[], yticks=[])
    ax.imshow(digits.images[i], cmap=plt.cm.binary)
    
    # label the image with the target value
    ax.text(0, 7, str(digits.target[i]))
#%%
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, random_state=0)
clf = DecisionTreeClassifier(max_depth=60)
clf.fit(Xtrain, ytrain)
ypred = clf.predict(Xtest)
metrics.accuracy_score(ypred, ytest)

#%%
def f(x:np.array):
    return 0
x=np.random.random(1000)
plt.hist(x)
plt.figure()
x=np.random.normal(0.5,0.1,1000)
plt.hist(x)
#%%
