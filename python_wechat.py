#!/usr/bin/evn python
# encoding: utf-8
# @version     : python 3.7
# @Time        :2019/9/23 10:13
# @Author      :Jiangbo Lin
# @Filename    :python_wechat.py 
# @Description :由于经常忘记家人的生日，所以利用itchat 以及mail服务
#发送提醒消息,用户需要自行修改收法邮件地址以及微信接收人的昵称，以及SMT服务的授权码
import itchat
import smtplib
import time
from email.mime.text import MIMEText
from email.header import Header
smtpserver = "smtp.qq.com"
smtpport = 465  #或者587

#可自行修改此处******************
mess_get_name = "xxxxx" #微信收到提醒的名字
from_mail = "xxxxx@qq.com"#发送端邮件
to_mail = ["xxxxxx@xx.com"]#接收端邮件
pw_code = "xxxxxxxxxxx"#用户修改授权码
#可自行修改此处*********************

send_time = 5#时间到等待5s 获取列表信息
man_nickname = []
women_nickname = []
other_nickname = []
timereminder = [ "09:00:00" ,
                 "12:00:00" ,
                 "16:00:00" ,
                 "18:00:00" ,
                 "11:28:00",
                 ]
def get_friends():
    friends = itchat.get_friends(update=True)[1:]
    return friends

def get_agendar(friend):
    global man_nickname
    global women_nickname
    global other_nickname
    for i in friend:
        if i['Sex'] == 1:
            man_nickname.append(i['NickName'])
        elif i['Sex'] == 0:
            women_nickname.append(i['NickName'])
        else:
            other_nickname.append(i['NickName'])
def wechat_send(message1):
     # 微信部分
     users = itchat.search_friends(mess_get_name)
     userName = users[0]['UserName']
     print(userName)
     itchat.send('生日提醒：'+message1, toUserName=userName)


def  wechat_sendtoroom(context):
    itchat.get_chatrooms(update=True)
    iRoom = itchat.search_chatrooms("xxxxxx")
    if len(iRoom) == 0:
        print("没有找到群")
    else:
        print(iRoom)
        chatroomname = iRoom[0]['UserName']
        print(iRoom[0]['UserName'])
        itchat.send_msg(context, chatroomname)


def mail_send(str_mess):
    message = MIMEText(str_mess, 'plain', 'utf-8')
    subject = '生日提醒'
    message['Subject'] = Header(subject, 'utf-8')
    try:
        smtp = smtplib.SMTP_SSL(smtpserver, smtpport)
        smtp.login(from_mail, pw_code)
        smtp.sendmail(from_mail, to_mail, message.as_string())
        print("邮件发送成功")
    except(smtplib.SMTPException) as e:
        print(e.message)
    finally:
        smtp.quit()
'''
    itchat.auto_login(hotReload=True)
    friend = get_friends()
    get_agendar(friend)
    for i in friend:
        print(i)
    print("我的微信总共有" + str(len(friend)) + "名好友！")
    print("男性：" + str(len(man_nickname)) + "名！")
    print("女性：" + str(len(women_nickname)) + "名！")
    print("其他：" + str(len(other_nickname)) + "名！")
    users = itchat.search_friends("")
    userName = users[0]['UserName']
    print(userName)
    localtime = time.asctime(time.localtime(time.time()))
    print("本地时间为 :", localtime)
    Flag = 1
    itchat.send('开始测试 每隔1分钟发送一次消息 连续发送5次', toUserName=userName)
    while Flag < 6:
        time.sleep(10)
        itchat.send('了', toUserName=userName)
        Flag += 1
    itchat.send('退出测试', toUserName=userName)
'''
if __name__ == '__main__':
    try_time = 2
    while True:
        admin_pw = input("请输入管理员密码：")
        if admin_pw == 'altran':
            print("输入正确")
            break
        else:
            if try_time !=0:
                print("密码输入错误，您还有%d 机会" % try_time)
                try_time -= 1
            else:
                print("连续3次错误，退出")
                exit()
    #itchat.auto_login(hotReload=True)#微信登陆
    brithday_file = open('brithday.txt', 'r', encoding="utf-8")#需要加txt的编码格式 否则不识别中文
    lines = len(brithday_file.readlines())
    if lines <= 2:#如果文件行数少于2行说明用户还未添加，请求添加
        print("**********************************************************************************")
        print("*********由于您未添加生日信息，请添加生日信息在  brithday.txt文件中********************")
        print("**********************************************************************************")
    brithday_file.seek(0)  # 重置光标位置
    #for i in brithday_file:
    #    print(i.rstrip())
    #brithday_file.close()
    print("********生日提醒程序开始运行********")
    while True:#循环扫描文件中的月日
        while True:
            Year_moth_day = time.strftime("%Y.%m.%d %H:%M:%S", time.localtime())
            if Year_moth_day[11:19] in timereminder:
                break
        brithday_file = open('brithday.txt', 'r', encoding="utf-8")  # 实时更新TXT文件
        time.sleep(send_time)

        brithday_file.seek(0)  # 重新制定光标位置
        str2 = "19";
        while True:
            line = brithday_file.readline()
            if line:
                if line.find("19")  != -1:#因为find函数找不到就会返回-1
                    brith = line[line.find("19")  :]
                    if brith[5:10] == Year_moth_day[5:10] :#判断生日已经到了
                        #print(Year_moth_day)
                        #print(Year_moth_day[11:13])
                        #if Year_moth_day[11:13] in timereminder.keys():
                        #       timereminder[Year_moth_day[11:13]] = 1
                        #        for key in timereminder.items():
                        #            print(key)
                        print("********************生日到了*****************************")
                        print(line)
                        print(Year_moth_day)
                        #wechat_send(line)#发送微信消息
                        mail_send("最诚挚的祝福，" + line + "生日快乐！！！！" )#发送mail消息
                        #wechat_sendtoroom("test")
            else:
                break
