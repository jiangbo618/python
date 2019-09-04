#!/usr/bin/evn python
# encoding: utf-8
# @version     : python 3.7
# @Time        :2019/7/25 14:29
# @Author      :Jiangbo Lin
# @Filename    :Mouse_control.py 
# @Description :

import pyautogui,time
'''
#下面这段程序可以显示鼠标的当前位置以X，Y坐标显示
try:
  while True:
    x, y = pyautogui.position()
    print(f'X坐标为：{x}  Y坐标为：{y} ' ,end='\r')#在同一行显示鼠标的X，Y坐标
except KeyboardInterrupt:
  print('\nExit.')
'''
click_positionx = 511
click_positiony = 348
def mouse_click(cur_x,cur_y) :
    pyautogui.click(x=cur_x, y=cur_y, button='left')

i = 0
while i <= 100 :
    mouse_click(click_positionx,click_positiony)
    #time.sleep(0.0001)
    i +=1
    print(i)
    

