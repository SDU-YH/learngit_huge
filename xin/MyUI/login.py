import tkinter as tk
from tkinter import messagebox
import sys
sys.path.append(r'./MyData')
import Data
from Data import *
import UI
from UI import *
class login_page:
    def __init__(self):
        self.login_window=tk.Tk()
        self.login_window.geometry("400x300+800+400")
        self.login_window.title('心理分析')
        self.canvas =  tk.Canvas(self.login_window,height = 200,width = 500)
        self.image_file = tk.PhotoImage(file = r'C:\Users\YH\Desktop\C_f.png')
        self.image = self.canvas.create_image(0,0,anchor = 'nw',image = self.image_file)
        self.canvas.pack(side = 'top')
        self.acc_label=tk.Label(self.login_window,text = 'Username:').place(x = 50,y = 160)
        self.pas_label=tk.Label(self.login_window,text = 'Password:').place(x = 50,y = 195)
        self.var_usr_name = tk.IntVar()
        #self.var_usr_name.set('Yh')
        self.var_usr_pwd = tk.IntVar()
        self.entry_usr_name = tk.Entry(self.login_window,textvariable = self.var_usr_name)
        self.entry_usr_name.place(x = 130,y = 160)
        self.entry_usr_pwd = tk.Entry(self.login_window,textvariable = self.var_usr_pwd,show ='*')
        self.entry_usr_pwd.place(x = 130,y = 195)
        self.btn_login = tk.Button(self.login_window,text = 'Login',command = self.usr_login)
        self.btn_login.place(x = 80,y = 230)
        self.btn_sign_up = tk.Button(self.login_window,text = 'Sign up')
        self.btn_sign_up.place(x = 180,y = 230)
        self.login_window.mainloop()

    def usr_login(self):
        self.data_from_web=Data_base('账户查询')
        self.A=self.data_from_web.get_handled_data()
        self.usr_name = self.var_usr_name.get()
        self.usr_pwd = self.var_usr_pwd.get()
        self.true_pwd='true'
        for i in range(len(self.A)):
            if self.A[i]['id']==self.usr_name:
                print("find it")
                self.true_pwd=self.A[i]['cnt']
        if self.true_pwd=='true':
            tk.messagebox.showwarning('账户不存在','请至官网注册账号')
        else:
            if self.usr_pwd==self.true_pwd:
               self.login_window.destroy()
               window = tk.Tk()
               BuDemo(window)
               window.mainloop()
            else:
               tk.messagebox.showerror('错误','密码错误')
