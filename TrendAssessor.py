# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 02:03:09 2020

@author: Rick
"""


import sqlalchemy as acm
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base= declarative_base()
class Question(Base):
    __tablename__= 'Question'
    id= acm.Column(acm.Integer, primary_key=True)
    question= acm.Column(acm.String)
    priority= acm.Column(acm.Integer)
    a1name= acm.Column(acm.String)
    a2name= acm.Column(acm.String)
    a3name= acm.Column(acm.String)
    a4name= acm.Column(acm.String)
    a5name= acm.Column(acm.String)
    a1value= acm.Column(acm.Integer)
    a2value= acm.Column(acm.Integer)
    a3value= acm.Column(acm.Integer)
    a4value= acm.Column(acm.Integer)
    a5value= acm.Column(acm.Integer)
    
    
    
    def __repr__(self):
        return '<Question(ques="%s",pri="%s")' % (self.question,self.priority)
    
    def GetAnswerValue(s,name):
        idx= s.GetAnswerNames().index(name)
        return s.GetAnswerValues()[idx]
    
    def GetAnswerNames(s):
        return [s.a1name,s.a2name,s.a3name,s.a4name,s.a5name]
    def GetAnswerValues(s):
        return [s.a1value,s.a2value,s.a3value,s.a4value,s.a5value]
    

    def GetValidAnswers(s):
        allanswers=[s.a1name,s.a2name,s.a3name,s.a4name,s.a5name]
        answers= []
        for answer in allanswers :
            if answer!=None:
                answers.append(answer)
            else:
                break
        return answers

engine= acm.create_engine("sqlite:///TrendAssessor.db")
Session= sessionmaker(bind=engine)
session=Session()

def GetQuestions():
    questions= session.query(Question).order_by(Question.priority)
    '''
    print(questions.count())
    for ques in questions:
        print(ques)
    '''
    return questions.all()

def Test():
    questions=GetQuestions()
    for ques in questions:
        print(ques.GetValidAnswers())
        
#Test()

