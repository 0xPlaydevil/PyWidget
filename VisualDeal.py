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
df['委托方向']=df['委托方向'].str.get(3)
df.loc[df['委托方向']=='出','direc']=-1
df.loc[df['委托方向']=='入','direc']=1
df['direc']=df['direc'].astype(float)
print(df['direc'].dtype)
df['trading_volumn']=df['成交金额'].mul(df['direc'])
print(df[['成交金额','direc','trading_volumn']])