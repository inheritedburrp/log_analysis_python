# coding: utf-8
import pandas as pd
import datetime
df=pd.read_csv('mainlog', sep=' ',  names=['timestamp','duration','ip','result','bytes','reqmthd','url','rfc','hierarchy', 'type'])
df['timestamp'].apply(datetime.datetime.fromtimestamp)
df.head(1)
df['timestamp']=map(datetime.datetime.fromtimestamp, df['timestamp'])
df.index=pd.to_datetime(df.pop('timestamp'))
df.head()
get_ipython().system(u'clear ')
df.head()
get_ipython().magic(u'pylab')
dummy = zeros((df.shape[0],))
myapply = lambda x: x +1
df['dummy'] = dummy
df['dummy'].apply(myapply)
df['dummy'].apply(myapply, inplace=True)
get_ipython().set_next_input(u"df['dummy'].apply");get_ipython().magic(u'pinfo apply')
get_ipython().set_next_input(u"df['dummy'].map");get_ipython().magic(u'pinfo map')
get_ipython().system(u'clear ')
df.head()
df.pop('dummy')
df.head()
df['duration'].plot()
get_ipython().system(u'clear ')
df['duration'].plot()
ylabel('Duration (seconds)')
(df['duration'] / 60.0).plot()
140000 / 3600
df['duration'] = df['duration'] / (1000.0)
df['duration'].plot()
df.index
df.head()
df.index.name
df.duration
df.duration.plot()
ylabel('Duration (seconds)')
title('Duration.')
title('Duration')
df.duration['06:00:00':'09:00:00']
df.index
df.index.head()
df.duration.head()
df.duration['2014-07-16 06:00':'2014-07-16 09:00']
df.duration['2014-07-16 06:00':'2014-07-16 09:00'].plot()
df.plot()
pd.scatter_matrix(df)
df.columns
df.plot('bytes', 'duration')
x = df.bytes
x = df.bytes.values
y = df.duration.values
plt.plot(x,y)
inds = np.argsort(x)
inds
y[inds]
x[inds]
plt.plot(x[inds], y[inds])
x.min()
x.max()
x.max() / 1000.0
x.max() / 1000.0 / 1000.0
get_ipython().magic(u'pinfo plt.plot')
plt.plot(np.log10(x), y)
plt.plot(np.log10(x[inds]), y[inds])
plt.xlabel('bytes (log)')
plt.ylabel('duration (ms)')
plt.title('Number of bytes transferred vs Duration')
df.head(1)
df['result'].nunique()
df['result'].value_counts()
df['result'].plot(kind='pie')
df['result'].value_counts().plot(kind='pie')
vc = df.result.value_counts()
vc
result = vc.index.copy()
get_ipython().system(u'clear ')
vc
vc['Other'] = 0
vc
vc[vc < 100]
vc[vc < 100].sum()
vc['Other'] = _
vc
vc.drop(vc<100)
vc.drop(vc<100, axis=0)
get_ipython().magic(u'pinfo vc.drop')
vc.drop(vc.index[vc<100], axis=0)
vc2 = _
vc2.plot(kind='pie')
def pieplot_thresh(N):
    pass
def pieplot_thresh(s, N):
    s['Other'] = 0
    s['Other'] = s[s<N].sum()
    s.drop(s.index[s<N]).plot(kind='pie')
    
vc
pieplot_thresh(vc, 1000)
pieplot_thresh(vc, 5000)
pieplot_thresh(vc, 5000)
def pieplot_thresh(s, N):
    s['Other'] = 0
    s['Other'] = s[s<N].sum()
    s.drop(s.index[s<N]).plot(kind='pie', autopct='%.2f')
    
pieplot_thresh(vc, 1000)
df.head(1)
df['ip'].plot(kind='pie')
df['ip'].value_count().plot(kind='pie', autopct='%.2f')
df['ip'].value_counts().plot(kind='pie', autopct='%.2f')
df['ip'].value_counts().plot(kind='bar', autopct='%.2f')
df['ip'].value_counts().plot(kind='bar')
df['ip'].value_counts().plot(kind='bar', rot=60)
df['ip'].value_counts().plot(rot=60)
df['ip'].value_counts().plot(rot=60)
df['ip'].value_counts().plot(rot=60, xlabel='ip addresses', ylabel='number of requests')
df['ip'].value_counts().plot(rot=60)
xlabel('ip address')
ylabel('request counts')
df['ip'].value_counts().plot(rot=20)
xlabel('ip address')
ylabel('request counts')
df.head()
df['reqmthd'].value_counts().plot(rot=20)
df['reqmthd'].value_counts().plot(kind='bar', rot=20)
ylabel('frequency counts')
xlabel('request methods')
df['reqmthd'].value_counts()
df['result'].value_counts()
