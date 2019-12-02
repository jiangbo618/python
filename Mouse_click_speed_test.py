#!/usr/bin/evn python
# encoding: utf-8
# @version     : python 3.7
# @Time        :2019/11/29 17:57
# @Author      :Jiangbo Lin
# @Filename    :Mouse_click_speed_test.py 
# @Description :
import tkinter as  tk
import time
from _pydecimal import Decimal, Context, ROUND_HALF_UP
#print(Context(prec=5, rounding=ROUND_HALF_UP).create_decimal('1.315097868'))
hit_flag = 0
start = 0
end = 0
text = ''
def  Check_mouse_speed(messageL):
    global hit_flag
    global start
    global end
    global text
    if hit_flag ==0:
        start = time.perf_counter()
        hit_flag =1
        var_username.set("开始")
        messageL["bg"] = "green"

    else:
        hit_flag = 0
        end = time.perf_counter()
        end =  end - start
        #print(Context(prec=5, rounding=ROUND_HALF_UP).create_decimal('1.315097868'))
        text = str(Context(prec=5, rounding=ROUND_HALF_UP).create_decimal(str(end))) + "s"
        var_username.set(text)
        messageL["bg"] = "red"

window = tk.Tk()
window.geometry('300x200')
window.title("Mouse Click Test")
var_username = tk.StringVar()
lablek = tk.Label(window,textvariable = var_username,bg=None)
lablek.place(x=120,y=50)#分开这样写 ，才可以设置颜色成功
tk.Button(window,text = 'Double click',command=lambda :Check_mouse_speed(lablek)).place(x=100,y=100)
window.mainloop()




