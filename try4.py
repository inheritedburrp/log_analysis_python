# coding: utf-8
import panda as pd
import pandas as pd
import matplotlib.pyplot as plt
import numpy
import datetime as dt
df= pd.read_csv('alllog', sep=' ', names=['timestamp','duration','ip','result','bytes','reqmthd','url','rfc','hierarchy', 'type'])
df['timestamp']=map(dt.datetime.fromtimestamp, df['timestamp'])
df.index=pd.to_datetime(df.pop('timestamp'))
df
arr=[]
for i in range(9,15):
    j=i+1
    p=len(df.ip['2014-07- 00:00'%i:'2014-07-16 23:59'%j])
    pass
for i in range(09,15):
    j=i+1
    p=len(df.ip['2014-07-%d 00:00'%i:'2014-07-%d 23:59'%j])
    arr.append(p)
    
for i in range(9,15):
    j=i+1
    p=len(df.ip['2014-07-%d 00:00'%i:'2014-07-%d 23:59'%j])
    arr.append(p)
    
len(arr)
arr
arr.index
arr.index()
brd=[]
for n in range(1,6):
pass
for n in range(1,6):
    brd.append(n)
    
brd
for n in range(1,7):
    brd.append(n)
    
brd
brd1=[]
for n in range(1,7):
    brd1.append(n)
    
brd1
brd1['wed','thu','fri','sat','sun','mon','tue','wed']
brd1=['wed','thu','fri','sat','sun','mon','tue','wed']
for i in range(9,16):
    j=i+1
    p=len(df.ip['2014-07-%d 00:00'%i:'2014-07-%d 23:59'%j])
    arr.append(p)
    
arr
for i in range(9,16):
    j=i+1
    p=len(df.ip['2014-07-%d 00:00'%i:'2014-07-%d 23:59'%j])
    arr.append(p)
    
arr1=[]
for i in range(9,16):
    j=i+1
    p=len(df.ip['2014-07-%d 00:00'%i:'2014-07-%d 23:59'%j])
    arr1.append(p)
    
arr1
plt.bar(brd1, arr1)
brd1=['wed','thu','fri','sat','sun','mon','tue']
plt.bar(brd1, arr1)
brd1=[1,2,3,4,5,6,7]
plt.bar(brd1, arr1)
plt.show()
