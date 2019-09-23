#!/usr/bin/evn python
# encoding: utf-8
# @version     : python 3.7
# @Time        :2019/9/23 10:13
# @Author      :Jiangbo Lin
# @Filename    :python_wechat.py 
# @Description :

import itchat
import sys,time,calendar
man_nickname = []
women_nickname = []
other_nickname = []
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
if __name__ == '__main__':
    itchat.auto_login(hotReload=True)
    friend = get_friends()
    get_agendar(friend)
    for i in friend:
        print(i)
    print("我的微信总共有"+ str(len(friend))+"名好友！")
    print("男性：" + str(len(man_nickname)) + "名！")
    print("女性：" + str(len(women_nickname)) + "名！")
    print("其他：" + str(len(other_nickname)) + "名！")
    users = itchat.search_friends("Momoo")
    userName = users[0]['UserName']
    print(userName)
    localtime = time.asctime( time.localtime(time.time()) )
    print("本地时间为 :", localtime)
    Flag = 1
    itchat.send('开始测试 每隔1分钟发送一次消息 连续发送5次', toUserName=userName)
    while Flag < 5 :
        time.sleep(60)
        itchat.send('老婆看娃辛苦了', toUserName=userName)
        Flag += 1
    itchat.send('退出测试', toUserName=userName)