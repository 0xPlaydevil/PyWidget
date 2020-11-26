# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 22:11:53 2020

@author: Rick
"""
sum= 0;
with open('workRecord.txt') as fp:
    for line in fp.readlines():
        idx= line.rfind('x',len(line)-8,len(line))
        if idx>=0:
            sum+= float(line.rstrip()[idx+1:len(line)])
        else:
            sum+= 1
print(sum)
print(sum*3)