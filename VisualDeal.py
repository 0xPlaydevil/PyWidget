# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 20:03:52 2021

@author: Rick
"""


import HoldAnalysis as hold
import matplotlib.pyplot as plt

dealRecs=hold.DealRecords()
df= dealRecs.take('三安光电')
df['direc']=df['委托方向']
# 提取委托方向
df['委托方向']=df['委托方向'].str.get(3)
df.loc[df['委托方向']=='出','direc']=-1
df.loc[df['委托方向']=='入','direc']=1
df['direc']=df['direc'].astype(float)
print(df['direc'].dtype)
# 为成交金额添加方向
df['trading_volumn']=df['成交金额'].mul(df['direc'])
print(df[['成交金额','direc','trading_volumn']])
# 翻转数据
df= df.iloc[::-1]
# 生成当前成本列
df['curcost']= df['trading_volumn'].cumsum()
print(df['curcost'])
# 生成收益列
df['profit']= df['股份余额']*df['成交均价']-df['curcost']
print(df['profit'])