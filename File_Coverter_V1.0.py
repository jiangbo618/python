#!/usr/bin/evn python
# encoding: utf-8
# @version     : python 3.7
# @Time        :2019/9/29 10:44
# @Author      :Jiangbo Lin
# @Filename    :file_transfer.py 
# @Description :

import os,sys,re,time
import binascii
#import getpass
import  tkinter  as tk
pw_123 = "gwz"
pw_user = 'gwz'
path_list = {}
try_time = 2
data_format = 0
bstr = []
var = None
blackground = None
pass_flag = 0

def con_file(root,name,sec_data,data):
    r_file = open(os.path.join(root, name),'rb')#原始文件
    w_file = open(os.path.join(root , "n_"+name),'wb+')
    r_file.seek(0)
    odd_data = 0
    #open
    while True:
        temp = r_file.read(1)
        if len(temp) == 0:
            if odd_data & 1 == 0:
                #print("这是一个偶数 %d " % odd_data)
                r_file.close()
                w_file.close()
                break
            else:
                #print("这是一个奇数 %d " % odd_data)
                r_file.close()
                w_file.close()
                break
        odd_data += 1
        if data == 1:# =0为byte读取 =1 为word 读取
            temp1 = r_file.read(1)
            if len(temp1) == 0:
                if odd_data & 1 == 0:
                    print("这是一个偶数 %d " % odd_data)
                    r_file.close()
                    w_file.close()
                    break
                else:
                    word_data = ord(temp)  # 只有低位
                    word_data = word_data ^ sec_data
                    str_data = bin(word_data)
                    if (len(str_data) - 2) > 8:
                        # bstr0 =  str_data[-8:]#low Byte
                        bstr0 = int(str_data[-8:], 2)
                        bstr1 = int(str_data[:-8], 2)

                    else:
                        bstr0 = int(str_data[:], 2)
                        bstr1 = 0  # 如果数据不足8bit 高位补0

                    # print(bstr0)
                    w_file.write(bytes([bstr0]))
                    w_file.write(bytes([bstr1]))
                    #print("这是一个奇数 %d " % odd_data)
                    r_file.close()
                    w_file.close()
                    break
            odd_data += 1
            word_data =  (ord(temp1) * 256 + ord(temp)) #将数据组合为16bit数据 然后异或
            #print(hex(word_data))
            word_data = word_data^ sec_data
            #print(hex(word_data))
            str_data = bin(word_data)
            if (len(str_data) - 2) > 8:
            #bstr0 =  str_data[-8:]#low Byte
                bstr0 = int(str_data[-8:], 2)
                bstr1 = int(str_data[:-8], 2)

            else:
                bstr0 = int(str_data[:], 2)
                bstr1 = 0 #如果数据不足8bit 高位补0

            #print(bstr0)
            #print(bstr1)
        #print(bstr0)
            w_file.write(bytes([bstr0]))
            w_file.write(bytes([bstr1]))
        else:
            w_file.write(bytes([ord(temp)^sec_data]))

        #hex_str = str(binascii.b2a_hex(temp))[2:-1]#b' 去除
        #file = "0x" + hex_str
        #print("0转换前："+file)
        #print("1转换后："+ str(hex(int(file, 16) ^ 255)))
        #w_file.write(bytes([int(file, 16) ^ 255]))
        #w_file.write(bytes([ord(temp)^sec_data]))#经整数写入
def conver_start(secdata,modedata,varmess,root1,messlable):
    index = 0
    #messlable.set("!!!!!!!!!转档开始!!!!!!!!!!")
    #root1.update()
    messlable['bg'] = 'white'
    root1.update()
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            if name.endswith(".a18") or name.endswith(".a16") or name.endswith(".a48") \
                    or name.endswith(".a32") or name.endswith(".bin"):
                # print(root)
                # time.sleep(2)
                # con_file(os.path.join(root, name),root,name)
                path_list[index] = [root, name]
                index += 1
                # print("{0}转换完成".format(os.path.join(root, name)))
    for key_value in path_list.values():
        print(key_value[0],key_value[1])
        varmess.set(key_value[1])
        root1.update()
        con_file(key_value[0], key_value[1], secdata, modedata)
    varmess.set("****文件转换完成****")
    messlable['bg'] = 'green'
    root1.update()

   # time.sleep(0.5)

def user_check(messageL,password):
    global try_time
    global pass_flag
    global window
    # admin_pw = input("请输入管理员密码：")
    # admin_pw = getpass.getpass("请输入密码：")
    if password != pw_123 :
        if try_time != 0:
            var.set(("用户名或密码输入错误,您还有%d次尝试机会！") % try_time)
            messageL["bg"] = "red"
            try_time -= 1
            pass_flag = 0
        else:
            exit()
    else:
        var.set("pass!!!")
        pass_flag = 1
        messageL["bg"] = "green"
        window.destroy()
        root1 = tk.Tk()
        root1.title('文件配置，作者：Jiangbo Lin')
        root1.geometry('500x300')  # 这里的乘是小x
        varmess = tk.StringVar()
        messlable = tk.Label(root1, textvariable=varmess,font=('Arial', 16))
        messlable.place(x=160,y=40)

        seclable = tk.Label(root1, text='请输入十进制加密数据')
        seclable.place(x=30, y=140)
        sec_data1 = tk.Entry(root1, font=('Arial', 14))  # 显示成明文形式
        sec_data1.place(x=160, y=140)
        rd_flag = tk.StringVar()
        rd_flag.set(1)#默认选择word 模式
        r1 = tk.Radiobutton(root1,text = 'Byte Mode',variable =rd_flag,value = 0)
        r1.place(x=20,y=60)
        r2 = tk.Radiobutton(root1,text = 'Word Mode',variable =rd_flag,value = 1)
        r2.place(x=20,y=80)
        startL = tk.Button(root1, text='GO',command=lambda :get_securty_data(sec_data1.get(),rd_flag.get(),varmess,root1,messlable) )
        startL.place(x=240, y=200)
        root1.mainloop()
def user_exit():
    time.sleep(0.1)
    exit()



def mkdir(path):
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")

    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path/'conver')

    # 判断结果
    if not isExists:
        os.makedirs(conver)

        print(' 创建成功')
        return True
    else:
        print( ' 目录已存在')
        return False


def get_securty_data(sec_data,modedata,varmess,root1,messlable):
    if sec_data.isdecimal():
        conver_start(int(sec_data),int(modedata),varmess,root1,messlable)
    else:
        varmess.set("输入非十进制纯数字，请重新输入！！！")



def get_data_format():
    while True:
        format_data = input("请输人0(byte) 或 1(word)：")
        if format_data.isdecimal() and (int(format_data) == 0 or int(format_data) == 1):
            return int(format_data)
        else:
            print("输入的非纯数字，Byte = 0  word = 1")
'''
def con_file(root,name,sec_data,data):
    r_file = open(os.path.join(root, name),'rb')#原始文件
    w_file = open(os.path.join(root , "n_"+name),'wb+')
    r_file.seek(0)
    odd_data = 0
    #open
    while True:
        temp = r_file.read(1)
        if len(temp) == 0:
            if odd_data & 1 == 0:
                #print("这是一个偶数 %d " % odd_data)
                r_file.close()
                w_file.close()
                break
            else:
                #print("这是一个奇数 %d " % odd_data)
                r_file.close()
                w_file.close()
                break
        odd_data += 1
        if data == 1:# =0为byte读取 =1 为word 读取
            temp1 = r_file.read(1)
            if len(temp1) == 0:
                if odd_data & 1 == 0:
                    print("这是一个偶数 %d " % odd_data)
                    r_file.close()
                    w_file.close()
                    break
                else:
                    word_data = ord(temp)  # 只有低位
                    word_data = word_data ^ sec_data
                    str_data = bin(word_data)
                    if (len(str_data) - 2) > 8:
                        # bstr0 =  str_data[-8:]#low Byte
                        bstr0 = int(str_data[-8:], 2)
                        bstr1 = int(str_data[:-8], 2)

                    else:
                        bstr0 = int(str_data[:], 2)
                        bstr1 = 0  # 如果数据不足8bit 高位补0

                    # print(bstr0)
                    w_file.write(bytes([bstr0]))
                    w_file.write(bytes([bstr1]))
                    #print("这是一个奇数 %d " % odd_data)
                    r_file.close()
                    w_file.close()
                    break
            odd_data += 1
            word_data =  (ord(temp1) * 256 + ord(temp)) #将数据组合为16bit数据 然后异或
            #print(hex(word_data))
            word_data = word_data^ sec_data
            #print(hex(word_data))
            str_data = bin(word_data)
            if (len(str_data) - 2) > 8:
            #bstr0 =  str_data[-8:]#low Byte
                bstr0 = int(str_data[-8:], 2)
                bstr1 = int(str_data[:-8], 2)

            else:
                bstr0 = int(str_data[:], 2)
                bstr1 = 0 #如果数据不足8bit 高位补0

            #print(bstr0)
            #print(bstr1)
        #print(bstr0)
            w_file.write(bytes([bstr0]))
            w_file.write(bytes([bstr1]))
        else:
            w_file.write(bytes([ord(temp)^sec_data]))

        #hex_str = str(binascii.b2a_hex(temp))[2:-1]#b' 去除
        #file = "0x" + hex_str
        #print("0转换前："+file)
        #print("1转换后："+ str(hex(int(file, 16) ^ 255)))
        #w_file.write(bytes([int(file, 16) ^ 255]))
        #w_file.write(bytes([ord(temp)^sec_data]))#经整数写入
'''
if __name__ == '__main__':
    #global var
    #global blackground
    #global pass_flag
    window = tk.Tk()
    var = tk.StringVar()
    # 第2步，给窗口的可视化起名字
    window.title('文件加密器V1.0')

    # 第3步，设定窗口的大小(长 * 宽)
    window.geometry('500x300')  # 这里的乘是小x
    # 第4步，创建Lable
    #tk.Label(window, text="User name:").place(x=60, y=100)
    tk.Label(window, text="PassWord:").place(x=60, y=140)
    # blackground = 'red'
    messageL = tk.Label(window, textvariable=var, bg=None)
    messageL.place(x=160, y=40)
    # 第5步，在图形界面上设定输入框控件entry并放置控件
    var_username = tk.StringVar()
    #user_name = tk.Entry(window, textvariable=var_username, show=None, font=('Arial', 14))  # 显示成密文形式
    #user_name.place(x=160, y=100)
    var_userpassword = tk.StringVar()
    password = tk.Entry(window, textvariable=var_userpassword, show='*', font=('Arial', 14))  # 显示成明文形式
    password.place(x=160, y=140)
    # e1.pack()
    # e2.pack()
    # 第6步，在图形界面上设定button
    #useryes = tk.Button(window, text='Yes')
    #useryes.place(x=160, y=200)
    #userexit = tk.Button(window, text='Exit', command=user_exit)
    #userexit.place(x=360, y=200)
    password.bind("<Return>",lambda event:user_check(messageL,var_userpassword.get()))  # 注意这里是Return而不是Ente
    window.mainloop()

'''
    index = 0
    data = get_data_format()
    #print(data)
    sec_data = get_securty_data()
    #print(sec_data)

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
        con_file(key_value[0],key_value[1],sec_data,data)
    print("**************文件转换完成******************")
    time.sleep(2)
'''

