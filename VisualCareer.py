# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 21:16:18 2020

@author: Rick
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random

rnds= []
with open("career_data.txt") as fp:
    for line in fp.readlines():
        # --------从这里开始---------
        
        # --------到这里结束---------
        print(line)
    

for i in range(16):
    rnds.append(random.randrange(10,50))
print(rnds)

df= pd.DataFrame(rnds,columns=["val"], index=range(16))
print(df)

fig,ax= plt.subplots()
ax.plot(df.index,df["val"],linestyle="dotted",label="rand")
