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

class BuDemo:
    def __init__(self, root):
        root.title("沙盘游戏分析系统")
        root.geometry("1000x490+300+150")
        self.myphoto=PhotoImage(file=r"C:\Users\YH\Desktop\A_f.png")
        self.RF = tk.Button(root,
                            activebackground="red",
                            anchor='n',
                            relief='raised',
                            text="心理分析",
                            fg="blue",
                            font=('Helvetica', 30),
                            image=self.myphoto,
                            compound="center",
                            command=self.get_game_name_page)
        self.RF.pack(side="left")
        self.myphoto2=PhotoImage(file=r'C:\Users\YH\Desktop\B_f.png')

        self.RF = tk.Button(root,
                            text="开始游戏",
                            fg="red",
                            image=self.myphoto2,
                            compound="center",
                            font=('Helvetica', 30),
                            command=self.openweb)
        self.RF.pack(side="left")
        self.Edata={}
        self.var_name=tk.StringVar()

    def get_game_name_page(self):
        #name_page = Nam
        
        self.name_page=tk.Toplevel()
        self.name_page.title("选择一个合适的名称")
        self.name_page.geometry('300x300+300+200')
        '''
        self.canvas =  tk.Canvas(self.name_page,height = 200,width = 500)
        self.image_file = tk.PhotoImage(file = r'C:\Users\YH\Desktop\wuse_f.png')
        self.image = self.canvas.create_image(0,0,anchor = 'nw',image = self.image_file)
        self.canvas.pack()'''
        self.name_label=tk.Label(self.name_page,text='请输入沙盘的名字:').place(x=50,y=80)
        self.namein=Entry(self.name_page,textvariable=self.var_name).place(x=50,y=100)
        self.b4=Button(self.name_page,text='确认名称',command=self.predict_rf)
        
        self.b4.place(x=80,y=150)
        self.name_page.mainloop()

    def predict_rf(self):
        self.class_name=self.var_name.get()
        print(self.class_name)
        self.name_page.destroy()
        self.nextpage=tk.Toplevel()
        self.nextpage.title("请回答问题")
        self.nextpage.geometry("900x900+500+250")
        
        self.Que_str=[
            '',
            '问题2',
            '问题3',
            '问题4',
            '问题5']
        self.Q=[]
        self.Op=self.get_answer_from_database()
        ''' 
        for que_str in self.Que_str:
            self.Q.append(question(self.nextpage,self.Op,que_str))
        '''
        for i in range(len(self.Que_str)):
            self.Q.append(question(self.nextpage,self.Op[i],self.Que_str[i]))
        self.button3=Button(self.nextpage,text="提交回答",command=self.updata)
        self.button3.pack()
        self.nextpage.mainloop()
    

    def openweb(self):
        webbrowser.open("https://lingxinyun.cn/psy/index.html#/HomePage")

    def updata(self):
        self.nextpage.destroy()
        print("要上传答案了")
        #root.destroy()
        #调用随机森林
        #调用随机森林分析数据

    def get_answer_from_database(self):
        print('get_answer')
        self.answer_from_database=[]
        if self.class_name=='我难忘的一堂课':
            self.answer_from_database=[['课桌','凳子','黑板','花盆','学生'],
                                        ['A','B','C','D','E'],
                                        ['A','B','C','D','E'],
                                        ['A','B','C','D','E'],
                                        ['A','B','C','D','E']
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