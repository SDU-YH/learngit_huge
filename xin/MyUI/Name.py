import tkinter as tk
from tkinter import messagebox
import sys
sys.path.append(r'./MyData')
import Data
from Data import *
import UI
from UI import *

class Name:
    def __init__(self):
        self.class_name_page=tk.Toplevel()
        self.class_name_page.geometry("400x300+800+400")
        self.class_name_page.title('沙盘名字')
        self.acc_label=tk.Label(self.class_name_page,text = '你的名字:').place(x = 50,y = 160)
        self.var_name = tk.StringVar()
        self.entry_name = tk.Entry(self.class_name_page,textvariable = self.var_name)
        self.entry_name.place(x = 130,y = 160)
        self.btn_login = tk.Button(self.class_name_page,text = '我起好了！',command = self.get_answer_from_database)
        self.btn_login.place(x = 80,y = 230)
        self.class_name_page.mainloop()

    def get_answer_from_database(self):
        self.game_name = self.var_name.get()
        self.class_name_page.destroy()
        print(self.game_name)
        

