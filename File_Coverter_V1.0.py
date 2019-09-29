#!/usr/bin/evn python
# encoding: utf-8
# @version     : python 3.7
# @Time        :2019/9/29 10:44
# @Author      :Jiangbo Lin
# @Filename    :file_transfer.py 
# @Description :

import os,sys,re,time
import binascii
import getpass
pw_123 = "gwz"
path_list = {}
try_time = 2
def con_file(root,name):
    r_file = open(os.path.join(root, name),'rb')#原始文件
    w_file = open(os.path.join(root, "n_"+name),'wb+')
    r_file.seek(0)
    #open
    while True:
        temp = r_file.read(1)
        if len(temp) == 0:
            r_file.close()
            w_file.close()
            break
        #print(hex(ord(temp)^255))
        #hex_str = str(binascii.b2a_hex(temp))[2:-1]#b' 去除
        #file = "0x" + hex_str
        #print("0转换前："+file)
        #print("1转换后："+ str(hex(int(file, 16) ^ 255)))
        #w_file.write(bytes([int(file, 16) ^ 255]))
        w_file.write(bytes([ord(temp)^255]))#经整数写入
if __name__ == '__main__':
    index = 0
    while True:
        #admin_pw = input("请输入管理员密码：")
        admin_pw = getpass.getpass("请输入密码：")
        if admin_pw == pw_123:
            print("输入正确")
            break
        else:
            if try_time !=0:
                print("密码输入错误，您还有%d 机会" % try_time)
                try_time -= 1
            else:
                print("连续3次错误，2秒后自动退出!!!")
                time.sleep(2)
                exit()
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
                if name.endswith(".a18") or name.endswith(".a16") or name.endswith(".a48")\
                   or name.endswith(".a32") or name.endswith(".bin"):
                    #print(root)
                    #time.sleep(2)
                    #con_file(os.path.join(root, name),root,name)
                    path_list[index] = [root,name]
                    index += 1
                    #print("{0}转换完成".format(os.path.join(root, name)))
    for key_value in path_list.values():
        print(key_value[0], key_value[1])
        con_file(key_value[0],key_value[1])
    print("**************文件转换完成******************")
    time.sleep(2)


