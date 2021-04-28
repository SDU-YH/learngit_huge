import tkinter as tk
from tkinter import *

class question(Checkbutton):
    def __init__(self,root,op,que):
        root.title('请回答问题：')
        root.geometry('700x500')
        self.L=Label(root,text=que)
        self.L.pack()
        self.v = []
        for i in op:
            self.v.append(IntVar())
        self.photopath0=r'C:\Users\YH\learngit\xin\image&data\M_I\\'+op[0]+'.PNG'
        self.answer_photo0=PhotoImage(file=self.photopath0)
        self.b0 = Checkbutton(root,image=self.answer_photo0,variable=self.v[0])
        self.b0.pack(side='left')
        self.photopath1=r'C:\Users\YH\learngit\xin\image&data\M_I\\'+op[1]+'.PNG'
        self.answer_photo1=PhotoImage(file=self.photopath1)
        self.b1 = Checkbutton(root,image=self.answer_photo1,variable=self.v[1])
        self.b1.pack(side='left')
        self.photopath2=r'C:\Users\YH\learngit\xin\image&data\M_I\\'+op[2]+'.PNG'
        self.answer_photo2=PhotoImage(file=self.photopath2)
        self.b2 = Checkbutton(root,image=self.answer_photo2,variable=self.v[2])
        self.b2.pack(side='left')
        self.photopath3=r'C:\Users\YH\learngit\xin\image&data\M_I\\'+op[3]+'.PNG'
        self.answer_photo3=PhotoImage(file=self.photopath3)
        self.b3 = Checkbutton(root,image=self.answer_photo3,variable=self.v[3])
        self.b3.pack(side='left')
        self.photopath4=r'C:\Users\YH\learngit\xin\image&data\M_I\\'+op[4]+'.PNG'
        self.answer_photo4=PhotoImage(file=self.photopath4)
        self.b4 = Checkbutton(root,image=self.answer_photo4,variable=self.v[4])
        self.b4.pack(side='left')
        #self.bu=Button(root,text='提交')
        #self.bu.pack()
    

