# coding: utf-8
import pandas as pd
import datetime
import matplotlib.pyplot as plt
df= pd.read_csv('mainlog', sep=' ', names=['timestamp','duration','ip','result','bytes','reqmthd','url','rfc','hierarchy', 'type'])
df['timestamp']= map(datetime.datetime.fromtimestamp, df['timestamp'])
df.index=pd.to_datetime(df.pop('timestamp'))
len(df)
df.ip.count_values()
df.ip.value_counts()
df.ip.nunique()
df.duration['2014-07-16 00:00':'2014-07-15 00:00']
df.duration['2014-07-16 00:00':'2014-07-15 00:00'].count_values()
df.duration['2014-07-16 00:00':'2014-07-15 00:00'].value_counts()
df.duration['2014-07-16 00:00':'2014-07-15 00:00'].len()
len(df.duration['2014-07-16 00:00':'2014-07-15 00:00'])
df.duration['2014-07-16 00:00':'2014-07-15 00:00']
df.duration['2014-07-16 00:00':'2014-07-15 00:00'].value_counts()
df.duration['2014-07-16 00:00':'2014-07-15 00:00'].nunique()
df.duration['2014-07-15 00:00':'2014-07-16 00:00'].nunique()
df.ip['2014-07-15 00:00':'2014-07-16 00:00'].nunique()
df.columns
df.index['2014-07-15 00:00':'2014-07-16 00:00'].nunique()
df.ip['2014-07-15 00:00':'2014-07-16 00:00'].nunique()
df.plot('bytes', 'duration')
plt.show()
x=df.bytes.values
y=df.duration.values
plot(x,y)
plt.plot(x,y)
plt.show()
col= df.bytes / df.duration
col
max(col)
df.columns
col.plot()
plt.show()
max(col)
min(col)
col.nunique()
col.sum()
len(col)
col.plot()
plt.show()
plt.count_values()
plt.value_counts()()
plt.value_counts()
col.value_counts()
df.col
df.pop('col')
df['col']=col
df[np.isfinite(df['col'])]
import numpy as np
df[np.isfinite(df['col'])]
df[np.isfinite(df['col'])].plot()
plt.show()
df.col[np.isfinite(df['col'])].plot()
plt.show()
max(df.col[np.isfinite(df['col'])])
df['col']= map(col/1000, df.col)
df['col']= map(col/1000, df['col'])
myapply = lambda x: x/1000
df['col'].apply(myapply)
max(col)
max(df.col[np.isfinite(df['col'])])
df.col.value_counts()
df.col.sum()
sum(df.col[np.isfinite(df['col'])])
sum(df.col[np.isfinite(df['col'])]) / 420159
