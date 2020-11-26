# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 22:08:42 2020

@author: Rick
"""
print(3*(2,3,4)+(5,6))

# 类C格式化
formatStr= "Would you like some %s?"
drink= "coffee"
print(formatStr % drink)

# 模板字符串
from string import Template
tmpl= Template("there's tips in line $lineSeq of book $bookName")
finalStr= tmpl.substitute(lineSeq=15,bookName="cookbook")
print(finalStr)

# format字符串
from math import pi
from math import e
fmt1= "The book <{}> has {} pages."
fmt2= "{0} {1} {2} {0} {1} {3}"
fmt3= "{name} is approximately {value:.2f}."
print(fmt1.format("cpp primer",706))
words= ["the","more","practice","proficient"]
print(fmt2.format(tuple(words)))
print(fmt3.format(value=pi,name="pi"))
print(f"Euler's constant is roughly {e}")

