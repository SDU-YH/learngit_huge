import tkinter as tk
from tkinter import *

class question(Checkbutton):
    def __init__(self,root,op,que):
        self.L=Label(root,text=que)
        self.L.pack()
        self.v = []
        for i in op:
            self.v.append(IntVar())
            self.b = Checkbutton(root,text=i,variable=self.v[-1])
            self.b.pack(anchor=W)