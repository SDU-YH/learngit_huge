import tkinter as tk
from tkinter import *
import matplotlib.pylab as pl
import webbrowser
import os
import turtle
from PIL import Image, ImageTk
import sys
sys.path.append(r'./MyData')
sys.path.append(r'./Tree')
'''
import RandomForest
from RandomForest import * '''
import Data_manage
from Data_manage import *
from Question import *
import Name
from Name import *
import Draw
from Draw import *

class BuDemo:
    def __init__(self,gggg):
        self.id=gggg
        self.root=tk.Tk()
        self.root.title("聆心云沙盘游戏分析系统")
        self.root.geometry("1000x490+300+150")
        self.myphoto=PhotoImage(file=r"C:\Users\YH\learngit\xin\image&data\A_f.png")
        self.myphoto2=PhotoImage(file=r'C:\Users\YH\learngit\xin\image&data\B_f.png')
        self.RF = tk.Button(self.root,
                            text="开始游戏",
                            fg="blue",
                            image=self.myphoto2,
                            compound="center",
                            font=('Helvetica', 30),
                            command=self.openweb)
        self.RF.pack(side="left")
        self.Edata={}
        self.var_name=tk.StringVar()
        self.RF = tk.Button(self.root,
                            activebackground="red",
                            anchor='n',
                            relief='raised',
                            text="心理分析",
                            fg="red",
                            font=('Helvetica', 30),
                            image=self.myphoto,
                            compound="center",
                            command=self.get_game_name_page)
        self.RF.pack(side="left")
        

       

    def get_game_name_page(self):
        #name_page = Nam
        
        self.name_page=tk.Toplevel()
        self.name_page.title("选择一个合适的名称")
        self.name_page.geometry('300x300+300+200')
        
        self.name_label=tk.Label(self.name_page,text='请输入沙盘的名字:').place(x=50,y=80)
        self.namein=Entry(self.name_page,textvariable=self.var_name).place(x=50,y=100)
        self.b4=Button(self.name_page,text='确认名称',command=self.predict_rf)
        
        self.b4.place(x=80,y=150)
        self.name_page.mainloop()

    def predict_rf(self):
        
        self.class_name=self.var_name.get()
        print(self.class_name)
        self.root.destroy()
        self.nextpage=tk.Tk()
        self.nextpage.geometry('700x500')
        self.nextpage.title("请回答问题")
        self.Q=[]
        self.Op=self.get_answer_from_database()
        '''
        for que_str in self.Que_str:
            self.Q.append(question(self.nextpage,self.Op,que_str))
        
        self.page=[]
        self.page1==tk.Toplevel()
        self.page2=tk.Toplevel()
        self.page3=tk.Toplevel()
        self.page4=tk.Toplevel()
        self.page5=tk.Toplevel()'''
        #for i in range(len(self.Que_str)):
        #self.Q.append(question(self.nextpage,self.Op[1],'你最喜欢的沙具'))
        self.L0=Label(self.nextpage,text='你最喜欢的沙具：')
        self.L0.pack()
        self.v = []
        op=self.Op[0]
        for i in op:
            self.v.append(IntVar())
        self.photopath0=r'C:\Users\YH\learngit\xin\image&data\M_I\\'+op[0]+'.PNG'
        self.answer_photo0=PhotoImage(file=self.photopath0)
        self.b0 = Checkbutton(self.nextpage,image=self.answer_photo0,variable=self.v[0])
        self.b0.pack(side='left')
        self.photopath01=r'C:\Users\YH\learngit\xin\image&data\M_I\\'+op[1]+'.PNG'
        self.answer_photo01=PhotoImage(file=self.photopath01)
        self.b01 = Checkbutton(self.nextpage,image=self.answer_photo01,variable=self.v[1])
        self.b01.pack(side='left')
        self.photopath02=r'C:\Users\YH\learngit\xin\image&data\M_I\\'+op[2]+'.PNG'
        self.answer_photo02=PhotoImage(file=self.photopath02)
        self.b02 = Checkbutton(self.nextpage,image=self.answer_photo02,variable=self.v[2])
        self.b02.pack(side='left')
        self.photopath03=r'C:\Users\YH\learngit\xin\image&data\M_I\\'+op[3]+'.PNG'
        self.answer_photo03=PhotoImage(file=self.photopath03)
        self.b03 = Checkbutton(self.nextpage,image=self.answer_photo03,variable=self.v[3])
        self.b03.pack(side='left')
        self.photopath04=r'C:\Users\YH\learngit\xin\image&data\M_I\\'+op[4]+'.PNG'
        self.answer_photo04=PhotoImage(file=self.photopath04)
        self.b04 = Checkbutton(self.nextpage,image=self.answer_photo04,variable=self.v[4])
        self.b04.pack(side='left')
        self.button3=Button(self.nextpage,text="下一题",command=self.Q1(self.Op[1])).place(x=300,y=340)
        self.nextpage.mainloop()
    
    def Q1(self,op):
        #self.nextpage.destroy()
        self.nextpage1=tk.Toplevel()
        self.nextpage1.title('请回答问题：')
        self.nextpage1.geometry('700x500')
        self.L1=Label(self.nextpage1,text='哪个沙具能代表你：')
        self.L1.pack()
        self.v1 = []
        for i in op:
            self.v1.append(IntVar())
        self.photopath10=r'C:\Users\YH\learngit\xin\image&data\M_I\\'+op[0]+'.PNG'
        self.answer_photo10=PhotoImage(file=self.photopath10)
        self.b10 = Checkbutton(self.nextpage1,image=self.answer_photo10,variable=self.v1[0])
        self.b10.pack(side='left')
        self.photopath11=r'C:\Users\YH\learngit\xin\image&data\M_I\\'+op[1]+'.PNG'
        self.answer_photo11=PhotoImage(file=self.photopath11)
        self.b11 = Checkbutton(self.nextpage1,image=self.answer_photo11,variable=self.v1[1])
        self.b11.pack(side='left')
        self.photopath12=r'C:\Users\YH\learngit\xin\image&data\M_I\\'+op[2]+'.PNG'
        self.answer_photo12=PhotoImage(file=self.photopath12)
        self.b12 = Checkbutton(self.nextpage1,image=self.answer_photo12,variable=self.v1[2])
        self.b12.pack(side='left')
        self.photopath13=r'C:\Users\YH\learngit\xin\image&data\M_I\\'+op[3]+'.PNG'
        self.answer_photo13=PhotoImage(file=self.photopath13)
        self.b13 = Checkbutton(self.nextpage1,image=self.answer_photo13,variable=self.v1[3])
        self.b13.pack(side='left')
        self.photopath14=r'C:\Users\YH\learngit\xin\image&data\M_I\\'+op[4]+'.PNG'
        self.answer_photo14=PhotoImage(file=self.photopath14)
        self.b14 = Checkbutton(self.nextpage1,image=self.answer_photo14,variable=self.v1[4])
        self.b14.pack(side='left')
        self.button4=Button(self.nextpage1,text="下一题",command=self.Q2(self.Op[2])).place(x=300,y=340)
        
        self.nextpage1.mainloop()

    def Q2(self,op):
        #self.nextpage1.destroy()
        self.nextpage2=tk.Toplevel()
        self.nextpage2.title('请回答问题：')
        self.nextpage2.geometry('700x500')
        self.L2=Label(self.nextpage2,text='最重要的沙具：')
        self.L2.pack()
        self.v2 = []
        for i in op:
            self.v2.append(IntVar())
        self.photopath20=r'C:\Users\YH\learngit\xin\image&data\M_I\\'+op[0]+'.PNG'
        self.answer_photo20=PhotoImage(file=self.photopath20)
        self.b20 = Checkbutton(self.nextpage2,image=self.answer_photo20,variable=self.v2[0])
        self.b20.pack(side='left')
        self.photopath21=r'C:\Users\YH\learngit\xin\image&data\M_I\\'+op[1]+'.PNG'
        self.answer_photo21=PhotoImage(file=self.photopath21)
        self.b21 = Checkbutton(self.nextpage2,image=self.answer_photo21,variable=self.v2[1])
        self.b21.pack(side='left')
        self.photopath22=r'C:\Users\YH\learngit\xin\image&data\M_I\\'+op[2]+'.PNG'
        self.answer_photo22=PhotoImage(file=self.photopath22)
        self.b22 = Checkbutton(self.nextpage2,image=self.answer_photo22,variable=self.v2[2])
        self.b22.pack(side='left')
        self.photopath23=r'C:\Users\YH\learngit\xin\image&data\M_I\\'+op[3]+'.PNG'
        self.answer_photo23=PhotoImage(file=self.photopath23)
        self.b23 = Checkbutton(self.nextpage2,image=self.answer_photo23,variable=self.v2[3])
        self.b23.pack(side='left')
        self.photopath24=r'C:\Users\YH\learngit\xin\image&data\M_I\\'+op[4]+'.PNG'
        self.answer_photo24=PhotoImage(file=self.photopath24)
        self.b24 = Checkbutton(self.nextpage2,image=self.answer_photo24,variable=self.v2[4])
        self.b24.pack(side='left')
        self.button5=Button(self.nextpage2,text="提交回答",command=self.get_class_name).place(x=300,y=340)
        self.nextpage2.mainloop()
    
    



    def openweb(self):
        webbrowser.open("https://lingxinyun.cn/psy/index.html#/HomePage")

    def get_class_name(self):#A:主题1，主题2，主题3
        if self.class_name=='我难忘的一堂课':
            A='主题1'
        if self.class_name=='我的一次生日派对':
            A='主题2'
        if self.class_name=='我可爱的一家人':
            A='主题3'
        if self.class_name=='我的一次旅行':
            A='主题4'
        if self.class_name=='我可爱的家乡':
            A='主题5'
        self.use_id_get_game_data=Get_gamedata(self.id)
        self.ffff=self.use_id_get_game_data.get_handled_data(A)

        print(self.ffff)

 

    def get_answer_from_database(self):
        print('get_answer')
        self.answer_from_database=[]
        if self.class_name=='我难忘的一堂课':

            self.answer_from_database=[['老爷爷','老奶奶','中年男人','中年女人','少年'],
                                        ['警察','消防员','中年男人','老爷爷','工程师'],
                                        ['工程师','中年女人','老奶奶','消防员','少年'],
                                        ['老爷爷','老奶奶','中年男人','中年女人','少年'],
                                        ['老爷爷','老奶奶','中年男人','中年女人','少年']
            ]
        if self.class_name=='我的一次生日派对':
            self.answer_from_database=[['蛋糕','蜡烛','果汁','打火机','凳子'],
                                        ['A','B','C','D','E'],
                                        ['A','B','C','D','E'],
                                        ['A','B','C','D','E'],
                                        ['A','B','C','D','E']
            ]
        if self.class_name=='我的一次旅行':
            self.answer_from_database=[['蛋糕','蜡烛','果汁','打火机','凳子'],
                                        ['A','B','C','D','E'],
                                        ['A','B','C','D','E'],
                                        ['A','B','C','D','E'],
                                        ['A','B','C','D','E']]
        if self.class_name=='我可爱的家乡':
            self.answer_from_database=[['蛋糕','蜡烛','果汁','打火机','凳子'],
                                        ['A','B','C','D','E'],
                                        ['A','B','C','D','E'],
                                        ['A','B','C','D','E'],
                                        ['A','B','C','D','E']]
        if self.class_name=='我可爱的一家人':
            self.answer_from_database=[['蛋糕','蜡烛','果汁','打火机','凳子'],
                                        ['A','B','C','D','E'],
                                        ['A','B','C','D','E'],
                                        ['A','B','C','D','E'],
                                        ['A','B','C','D','E']]
        return self.answer_from_database