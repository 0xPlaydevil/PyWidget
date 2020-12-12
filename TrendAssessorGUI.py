# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 13:00:07 2020

@author: Rick
"""
from TrendAssessor import Question
import PySimpleGUI as sg

class QuestionWidget:
    def __init__(self,question):
        ques_info= question
        layout=[[sg.text(ques_info.question)]]
        answers= ques_info.GetAnswers()
        
        for i in range(ques_info.)
        layout.append([sg.text(ques_info.question)])
    
    
    
    

