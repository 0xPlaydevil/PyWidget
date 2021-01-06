# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 13:00:07 2020

@author: Rick
"""
import TrendAssessor as TrdAsr
import PySimpleGUI as SG
import time

class QuestionWidget:
    def __init__(self,question):
        self.ques_info= question
        self.layout=[[SG.Text(self.ques_info.question)]]
        '''
        answers= ques_info.GetValidAnswers()
        lElems= []
        for ans in answers:
            lElems.append(SG.Radio(ans, 0))
        '''
        self.layout.append([SG.Radio(ans,self.ques_info.id) for ans in self.ques_info.GetValidAnswers()])

line1=[]
line1+=[SG.Text('Code'),SG.Input(size=(15,1))]
line1.append(SG.Text(' '*30))
line1+=[SG.Text(time.strftime('%a |    %b %d |    %H:%M:%S |',time.localtime()),key='_lbTime_')]
layout= [line1,[SG.HorizontalSeparator()]]

for ques in TrdAsr.GetQuestions():
    quesUI= QuestionWidget(ques)
    layout+= quesUI.layout
layout.append([SG.HorizontalSeparator('gray')])
win= SG.Window("TrendAssessor",layout,size=(800,600),grab_anywhere=True,icon='Trend.ico')
win.AddRow(SG.Button('toplevel'),SG.Slider((0.1,1),0.8,0.1,0.2,'h',key='_sldAlpha_',enable_events=True))

while(True):
    event,values= win.Read(1000)
    if(event==SG.WIN_CLOSED):
        break
    if event=='toplevel':
        win.alpha_channel=0.5
    if event=='_sldAlpha_':
        win.alpha_channel=values['_sldAlpha_']
    win.Element('_lbTime_').Update(time.strftime('%a |    %b %d |    %H:%M:%S |',time.localtime()))
win.Close()
    
    
    
    

