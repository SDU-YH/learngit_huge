import tkinter as tk
from tkinter import messagebox
import sys
#sys.path.append(r'./UI')
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
        self.var_usr_name = tk.StringVar()
        self.var_usr_name.set('Yh')
        self.var_usr_pwd = tk.StringVar()
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
        self.usr_name = self.var_usr_name.get()
        self.usr_pwd = self.var_usr_pwd.get()
        if self.usr_pwd=='123':
            self.login_window.destroy()
            window = tk.Tk()
            BuDemo(window)
            window.mainloop()
            
        else:
            tk.messagebox.showerror('错误','密码错误')
           

login_page()