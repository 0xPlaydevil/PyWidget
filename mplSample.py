# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 19:07:48 2020

@author: Rick
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import yfinance as yf
# %matplotlib

df_amd = yf.download('AMD', start='2019-01-02', end='2020-01-01', progress=False)
print(df_amd)

df = df_amd[['Adj Close']] #这里要用两个[]，否则是一个series而不是df
df['s_r'] = df/df.shift(1)-1 #计算简单收益率
df.rename(columns={'Adj Close':'adj_close'},inplace=True) #更改columns
df_rolling = df[['s_r']].rolling(window=21).agg(['mean', 'std']) #以21天为窗口期，计算窗口期内的平均值和标准差
df_rolling.columns = df_rolling.columns.droplevel() #columns标签有两层，去掉外面的一层
df_abnorm = df.join(df_rolling) #合并数据
def scout(row): #这个函数用来找出异常值
    rtn = row['s_r']
    mean = row['mean']
    std = row['std']
    if (rtn > mean + 3 * std) or (rtn < mean - 3 * std):
        return 1
    else:
        return 0

df_abnorm['abnorm'] = df_abnorm.apply(scout, axis=1)
abnorm = df_abnorm[df_abnorm['abnorm'] == 1]['s_r']


def on_pick(event):
    ind = event.ind[0] #ind是一个list，这点一定注意
    x = event.mouseevent.xdata
    y = event.mouseevent.ydata
    date = abnorm.index[ind]
    string_date = 'The date is %s, and the simple return is %s' % (date.date(), round(y, 2))
    plt.title(string_date)
    fig.canvas.draw()
    
    
fig, ax = plt.subplots(figsize=(12,8))
ax.plot(df_abnorm.index, df_abnorm.s_r, color='blue', label='Normal')
ax.scatter(abnorm.index, abnorm.values, picker=5, color='red', label='Abnormal')
ax.set_title("AMD stock ananlysis")
ax.legend(loc='upper left')
fig.canvas.mpl_connect('pick_event', on_pick)
plt.show()