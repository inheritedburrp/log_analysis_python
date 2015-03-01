# coding: utf-8
import pandas as pd
import datetime
import numpy as np
data=pd.read_csv('mainlog', sep=' ', header=header_rows)
header_rows=['timestamp','duration','ip','result','bytes','reqmthd','url','rfc','hierarchy', 'type']
data=pd.read_csv('mainlog', sep=' ', header=header_rows)
data=pd.read_csv('mainlog', sep=' ', header=header_rows)
data=pd.read_csv('mainlog', sep=' ', header=None)
data=pd.read_csv('mainlog', sep=' ', header=header_rows)
name_rows
data.head()
data=('mainlog', sep= ' ', header=header_rows)
data=('mainlog', sep=' ', header=header_rows)
data= pd.read_csv('mainlog', sep=' ', names=header_rows)
df =pd.DataFrame(data)
df
df['timestamp'][0]
df['timestamp']= map(datetime.datetime.fromtimestamp, df['timestamp'])
df.head(2)
df.index
df[0:2]
df[10:20]
df.index
df.index=pd.to_datetime(df.pop('timestamp'))
df.index
header_rows
df['duration'].plot()
import matplotlib.pyplot as plt
plt.show()
import matplotlib.pyplot as plt
df['duration'].plot()
plt.show()
grouped_ip=df.groupby('ip')
grouped_ip.head()
grouped_results=df.groupby('result')
grouped_results.head(2)
grouped_type=df.groupby('type')
grouped_type.head()
grouped_type.size()
grouped_type.value_counts()
grouped_type.count_values()
get_ipython().magic(u'save my_usefull_session 1-42')
