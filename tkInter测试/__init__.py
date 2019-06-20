#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from tkinter import *    #注意模块导入方式，否则代码会有差别

class App:
    def __init__(self, master):
        #使用Frame增加一层容器
        fm1 = Frame(master)
        #Button是一种按钮组件，与Label类似，只是多出了响应点击的功能
        Button(fm1, text='Top').pack(side=TOP, anchor=W, fill=X, expand=YES)
        Button(fm1, text='Center').pack(side=TOP, anchor=W, fill=X, expand=YES)
        Button(fm1, text='Bottom').pack(side=TOP, anchor=W, fill=X, expand=YES)
        fm1.pack(side=LEFT, fill=BOTH, expand=YES)

        fm2 = Frame(master)
        Button(fm2, text='Left').pack(side=LEFT)
        Button(fm2, text='This is the Center button').pack(side=LEFT)
        Button(fm2, text='Right').pack(side=LEFT)
        fm2.pack(side=LEFT, padx=10)


root = Tk()
root.title("Pack - Example")
display = App(root)
root.mainloop()