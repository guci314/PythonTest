#%%
import numpy as np
from numpy import array
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.utils import Bunch
from IPython.display import display
from pandas import DataFrame
from sklearn.linear_model import LinearRegression
from sklearn import neighbors, datasets
from sklearn.svm import SVC,SVR
from sklearn.linear_model import LinearRegression

#region test
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
x=np.arange(10)
x+=10
y=np.sum(x)
y=np.mean(x)
print(y)
#%%
try:
    x=5/0
except Exception as e:
    print(e)


#%%
# initialize list of lists 
data = [['tom', 10], ['nick', 15], ['juli', 14]] 
  
# Create the pandas DataFrame 
df = pd.DataFrame(data, columns = ['Name', 'Age']) 
  
# print dataframe. 
df

#%%
# intialise data of lists. 
data = {'Name':['Tom', 'nick', 'krish', 'jack'], 'Age':[20, 21, 19, 18]} 
  
# Create DataFrame 
df = pd.DataFrame(data) 

# Print the output.  

#%%
# initialise data of lists. 
data = {'Name':['Tom', 'Jack', 'nick', 'juli'], 'marks':[99, 98, 95, 90]} 
  
# Creates pandas DataFrame. 
df = pd.DataFrame(data, index =['rank1', 'rank2', 'rank3', 'rank4']) 
  
# print the data 
df 

#%%
data=[[1,2,3],[4,5,6],[7,8,9]] 
# Creates DataFrame. 
df1 = pd.DataFrame(data) 
df1.columns=['x','y','z']  
# Print the data 
display(df1)

#endregion

#%%
iris:Bunch = load_iris()

x_index = 2
y_index = 1
# this formatter will label the colorbar with the correct target names
formatter = plt.FuncFormatter(lambda i, *args: iris.target_names[int(i)])

plt.scatter(iris.data[:, x_index], iris.data[:, y_index],
            c=iris.target, cmap=plt.cm.get_cmap('RdYlBu', 3))
plt.colorbar(ticks=[0, 1, 2], format=formatter)
plt.clim(-0.5, 2.5)
plt.xlabel(iris.feature_names[x_index])
plt.ylabel(iris.feature_names[y_index])

#%%
np.random.seed(0)
data=np.random.random(size=100)*3
target=data*2+1
deviation=np.random.randn(100)
plt.hist(deviation,bins=20,density=True)
plt.figure()
target=target+deviation
plt.scatter(data,target)
#model=LinearRegression()
model = SVR()
model.fit(data[:,np.newaxis],target)
testData=np.linspace(0, 3, 100)
testResult=model.predict(testData[:,np.newaxis])
plt.plot(testData,testResult,'r+')

#%%
df=pd.read_csv('sklearn_pycon2015/notebooks/pokemon_data.csv')
df.head()

#%%
df.loc[df['Type 1']=='Grass']