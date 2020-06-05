#!/usr/bin/evn python
# encoding: utf-8
# @version     : python 3.7
# @Time        :2019/7/25 14:29
# @Author      :Jiangbo Lin
# @Filename    :Mouse_control.py 
# @Description :

import pyautogui,time,os

classindex = 0 #在学课程中的课程
sectionindex = 0#课程中的章节

#下面这段程序可以显示鼠标的当前位置以X，Y坐标显示
'''
while True:
    x, y = pyautogui.position()
    print(f'X坐标为：{x}  Y坐标为：{y} ' ,end='\r')#在同一行显示鼠标的X，Y坐标
#except KeyboardInterrupt:
#  print('\nExit.')
'''
arrow_postion = [1000,50]
frash_postion = [1055,54]
speedup_position = [1297,266]
center_play = [1178,172]
def mouse_leftclick(cur_x,cur_y) :
    pyautogui.click(x=cur_x, y=cur_y, button='left')

def mouse_dropTo(cur_x,cur_y,time) :
    pyautogui.dragTo(x=cur_x, y=cur_y,duration=time)



def mouse_moveTo(cur_x,cur_y) :
    pyautogui.moveTo(x=cur_x, y=cur_y,duration=0.1)


def play_section():
    i = 0
    while i < 4:  # 点四下进入加速
        time.sleep(0.5)
        mouse_leftclick(speedup_position[0], speedup_position[1])
        i += 1


def play_class_section():
    time.sleep(0.5)#wait refresh
    class_location = pyautogui.locateOnScreen('picture/ChooseClass.PNG',grayscale=True)  # 找到箭头图片
    if class_location != None:  # 如果没有找到课程图片
        print(class_location)
        class_x, class_y = pyautogui.center(class_location)  # 分析选课坐标
        print("class_x :" + str(class_x) + " class_y :" + str(class_y))
        mouse_moveTo(class_x,class_y)
        time.sleep(1)
        mouse_dropTo(arrow_postion[0]+100,arrow_postion[1]-200,3)


        #mouse_leftclick(class_x+10 , class_y + 90)  ;# 点击section
        #play_section()
        time.sleep(900)
    else:
        print("课程未找到错误")
        exit()
#pic_2 = pyautogui.screenshot('my_screenshot.png')
#time.sleep(1)
while True:
    clock_location = pyautogui.locateOnScreen('picture/clock.png',grayscale=True)#钟表图片
    if clock_location != None:#如果没有找到钟表图片，表示学习完成
        print(clock_location)
        clock_x,clock_y = pyautogui.center(clock_location)#分析钟表坐标
        print("clock x :" + str(clock_x) + " clock Y :" + str(clock_y))
        mouse_leftclick(clock_x - 100 , clock_y)#点击开始课程
        play_class_section()
    else:
        Year_moth_day = time.strftime("%Y.%m.%d %H:%M:%S", time.localtime())
        print("*************学习完成************"+ Year_moth_day )#此处添加学习时间和完成时间
        break

'''
arrow_location = pyautogui.locateOnScreen('picture/arrow.png')#载入箭头图片
print(arrow_location)
index_x,index_y = pyautogui.center(arrow_location)#分析箭头坐标
print("arrow x :" + str(index_x) + " arrow Y :" + str(index_y))

number7_location = pyautogui.locateOnScreen('picture/ChooseClass.png')
print(number7_location)
choosex,choosey = pyautogui.center(number7_location)
print("choose class x :" + str(choosex) + "choose class Y :" + str(choosey))
mouse_moveTo(choosex,choosey)
mouse_dropTo(index_x,index_y +30)
mouse_leftclick(index_x,index_y+80)
#while True:
#    x, y = pyautogui.position()
#    print(f'X坐标为：{x}  Y坐标为：{y} ' ,end='\r')

window_size =[]
click_positionx = 923
click_positiony = 73
class_y = 158
class_index = 0
def mouse_click(cur_x,cur_y) :
    pyautogui.click(x=cur_x, y=cur_y, button='left')
time.sleep(5)
while class_index <4:
    mouse_click(978,class_y + class_index*100)#start
    time.sleep(1)
    mouse_click(1127,237)#go
    i = 0
    while i<4:
        mouse_click(1289, 347)  # fast
        time.sleep(0.1)
        i += 1
    time.sleep(300)
    mouse_click(click_positionx,click_positiony)#exit
    class_index += 1
'''




