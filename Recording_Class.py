#!/usr/bin/evn python
# encoding: utf-8
# @version     : python 3.7
# @Time        :2020/2/27 9:39
# @Author      :Jiangbo Lin
# @Filename    :Recording_Class.py 
# @Description :
import pyautogui,time,os
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


smtpserver = "smtp.qq.com"
smtpport = 465  #或者587
from_mail = "179793236@qq.com"#发送邮件地址
to_mail = ["179793236@qq.com"]#接受邮件地址
pw_code = "cguynamibytccaee"#qq邮箱授权码

pictureph = "picture/screenshot.png"

classindex = 0 #在学课程中的课程
sectionindex = 0#课程中的章节

#下面这段程序可以显示鼠标的当前位置以X，Y坐标显示
#try:
ball_postion = [1215,22]
start_postion = [1255,22]
stop_postion = [1287,22]

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

def mail_send(str_mess):
    content =  str_mess
    textApart = MIMEText(content)
#..........................发送图片
    imageFile = pictureph
    imageApart = MIMEImage(open(imageFile, 'rb').read(), imageFile.split('.')[-1])
    imageApart.add_header('Content-Disposition', 'attachment', filename=imageFile)
    message = MIMEMultipart()
    message.attach(textApart)
    message.attach(imageApart)
    message['Subject'] = 'DV 培训课程'
    # ..........................发送图片
    try:
        #smtp = smtplib.SMTP_SSL(smtpserver, smtpport)
        smtp = smtplib.SMTP('smtp.qq.com')
        smtp.login(from_mail, pw_code)
        smtp.sendmail(from_mail, to_mail, message.as_string())
        print("邮件发送成功")
    except(smtplib.SMTPException) as e:
        print(e.message)
    finally:
        smtp.quit()


def Recording_function(hours,minute,second):
    time.sleep(10)
    mouse_moveTo(ball_postion[0], ball_postion[1])
    print("step1 find icon")
    time.sleep(3)
    mouse_leftclick(start_postion[0], start_postion[1])
    print("step2 start record")
    print(time.strftime("%Y.%m.%d %H:%M:%S", time.localtime()))
    time.sleep(hours * 3600 + minute * 60 + second)#录制时间
    mouse_moveTo(ball_postion[0], ball_postion[1])
    pyautogui.screenshot(pictureph)#截图发给用户确认
    print("step3 find icon again ")
    time.sleep(2)
    mouse_leftclick(stop_postion[0], stop_postion[1])
    print("step3 stop recording ")
    print(time.strftime("%Y.%m.%d %H:%M:%S", time.localtime()))

#time.sleep(1)
#第一步自行进入在学课程，找到需要学习的课程
if __name__ == '__main__':
    Recording_function(0,0,6)

    mail_send(time.strftime("%Y.%m.%d %H:%M:%S", time.localtime()) + "课程录制完毕")
    exit()
