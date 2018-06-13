#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    1 tkinter做一个界面 1.0
        1 创建一个tk对象
        2 创建主窗口，设置大小，以及背景颜色
        3 创建一个主要的框架，用pack，加入主窗口中
        4 创建lebal标题，entry输入框，button搜索按钮，text文本显示框。将他们用grid方法加入到frame中
        5 button 按钮绑定一个调用搜索函数，
        6 搜索函数自动获得输入值，然后调用后台request模块进行数据获取分析
        7 text文本模块绑定显示函数，函数自动调用html模块中的分析结果，返回显示
'''
import tkinter as tk
from tkinter import font

import reptile_request_v1
import my_soup_parse_html_v1




class Destkop():
    def text_string(self):
        '''这个方法，打开文件，获取分析后的数据。并将其返回'''
        show_str = ""
        with open("show_data.txt",encoding="utf-8") as f:
            for line in f.readlines():
                show_str+=line
        return show_str

    def sou(self):
        '''这个函数会获取关键字，调用request，到百度请求数据'''
        #搜索函数自动获得输入值，然后调用后台request模块进行数据获取分析
        asy_date = self.shu_entry.get()
        #调用request模块
        r=reptile_request_v1.my_request(asy_date,count=10)
        r.write_html()
        #判断关键字是否为空，为空，那么就不进行搜索
        if not asy_date.strip():
            return
        #创建数据分析对象，对数据进行分析
        my_parse_html=my_soup_parse_html_v1.Bsoup_html()
        my_parse_html.run_to_txt()
        #调用数据获取方法
        s=self.text_string()
        #将数据写到text区域显示
        self.result_text.delete(1.0,tk.END)
        self.result_text.insert(1.0, self.text_string())

    def __init__(self):
        # 1 创建一个tk对象
        self.top = tk.Tk()
        # 2 创建主窗口，设置大小，以及背景颜色,背景图片等
        self.top.title("关键字分析")
        self.top.maxsize(800, 1000)
        self.top.minsize(300, 500)

        self.pho = tk.PhotoImage(file="image/nav2.gif")
        text_bg = tk.PhotoImage(file="image/bg_text.gif")
        self.ft = font.Font(family="Courier New", size=50, weight=font.BOLD)
        self.ft2 = font.Font(family="Courier New", size=30, weight=font.BOLD)
        # 3 创建一个主要的框架，用pack，加入主窗口中
        frame_1 = tk.Frame(self.top, bg="blue", width="500", height="200")
        frame_1.pack()
        frame_2 = tk.Frame(self.top, bg="green", width="500", height="200")
        frame_2.pack()
        frame_3 = tk.Frame(self.top, bg="red", width="500", height="200")
        frame_3.pack()

        # # 4 创建lebal标题，
        show_label = tk.Label(frame_1, bg="red", text="分析关键字", image=self.pho, compound="center", fg="black", font=self.ft)
        show_label.pack()
        # # entry输入框，
        self.shu_entry = tk.Entry(frame_2, bg="white", width="18", text="wokao", font=self.ft2, fg="gray",
                             relief="groove",
                             selectbackground="blue", highlightthickness="10", selectforeground="black",
                             selectborderwidth="10", bd="10",
                             highlightcolor="red", textvariable="请输入关键字", highlightbackground="green")
        self.shu_entry.grid(row=0, column=0)
        # button搜索按钮,# 5 button 按钮绑定一个调用搜索函数，
        sou_button = tk.Button(frame_2, bg="purple", width="8", font=self.ft2, text="分析", command=self.sou,
                               relief="groove", bd="10",
                               highlightbackground="blue", highlightcolor="red", highlightthickness="10")
        sou_button.grid(row=0, column=1)
        # text文本显示框。
        self.result_text = tk.Text(frame_3, bg="white", width="85", height="35")
        self.result_text.pack(side=tk.LEFT)

        #加载滚动条
        scrollbar=tk.Scrollbar(frame_3)
        scrollbar.pack(side=tk.RIGHT,fill=tk.Y)
        scrollbar.config(command=self.result_text.yview)
        self.result_text.config(yscrollcommand=scrollbar.set)



if __name__ == "__main__":

    d = Destkop()
    d.top.mainloop()

