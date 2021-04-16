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
                            #height=10,
                            #width=34,
                            command=self.predict_rf)
        self.RF.pack(side="left")
        self.myphoto2=PhotoImage(file=r'C:\Users\YH\Desktop\B_f.png')

        self.RF = tk.Button(root,
                            text="开始游戏",
                            fg="red",
                            image=self.myphoto2,
                            compound="center",
                            font=('Helvetica', 30),
                            #height=10,
                            #width=34,
                            command=self.openweb)
        self.RF.pack(side="left")
        self.Edata={}

    def predict_rf(self):
        self.nextpage=tk.Tk()
        self.nextpage.title("请回答问题")
        self.nextpage.geometry("900x900+500+250")
        Que_str=[
            '问题1',
            '问题2',
            '问题3',
            '问题4',
            '问题5']
        self.Q=[]
        self.Op=['A','B','C','D','E']
        for que_str in Que_str:
            self.Q.append(question(self.nextpage,self.Op,que_str))
        self.button3=Button(self.nextpage,text="提交回答",command=self.updata)
        self.button3.pack()
        self.nextpage.mainloop()
    
        
    def openweb(self):
        webbrowser.open("https://lingxinyun.cn/psy/index.html#/HomePage")

    def updata(self):
        self.Edata[1]=self.E1.get()
        self.Edata[2]=self.E2.get()
        self.Edata[3]=self.E3.get()
        self.Edata[4]=self.E4.get()
        self.Edata[5]=self.E5.get()
        self.nextpage.destroy()
        #调用随机森林
        #调用随机森林分析数据

        
