#%%
import stanfordnlp
from stanfordnlp.pipeline.doc import Sentence,Document
pipline=stanfordnlp.Pipeline(lang="zh")
s1='2018年8月，因为做生意资金短缺，成都市民王倩向4款APP贷款了2万元。没想到，这笔贷款竟成为了她的噩梦，此后越滚越多，截至今年5月，王倩称她一共还款100多万元'
doc:Document=pipline(s1)
sent:Sentence=doc.sentences[0]
sent.print_dependencies()
print('dfdfdf111')

#%%
s2="这是一个中文测试语句"
doc=pipline(s2)
sent1:Sentence=doc.sentences[0]
sent1.print_words()
print("finished")

#%%
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

x = np.linspace(0, 20, 100)
plt.plot(x, np.sin(x))
plt.show() 

#%%
class XXX:
    def f(self):
        print("qqqqqqqqqqqqqqqqqqq")

class BBB:
    """
    ccccccccccccccccccc
    """
    def f(self):
        print('bbbbbbbbbbb')

x=XXX()
x.f()
b=BBB()
b.f()
x.f()

#%%
s='ppppppppppp'
print(s)


#%%

import pandas as pd
import quandl

df = quandl.get("WIKI/GOOGL")

print(df.head())


#%%
df = df[['Adj. Open',  'Adj. High',  'Adj. Low',  'Adj. Close', 'Adj. Volume']]
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Low']) / df['Adj. Close'] * 100.0
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0
df = df[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]
print(df.head())

#%%
df.keys()

#%%
