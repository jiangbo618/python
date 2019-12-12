#!/usr/bin/evn python
# encoding: utf-8
# @version     : python 3.7
# @Time        :2019/12/3 10:44
# @Author      :Jiangbo Lin
# @Filename    :File_Insert_Data.py
# @Description :选择任意格式的二级制文件，往文件任意位置插入任意个数的随机数，在使用工作的目录产生
#相应的信息文件。：

import os,time
import random
import struct
#import  tkinter  as tk
random_list = []
#from tkinter.filedialog import askopenfilename
def selectpath():
    path_ = askopenfilename()
    path.set(path_)

def con_files(root,name,data_position,random_list):
    r_file = open(os.path.join(root, name),'rb')#原始文件
    w_file = open(os.path.join(root , "n_"+name),'wb+')
    #inf_file = os.path.join(root,"Information_file.txt")
    #if not os.path.exists(inf_file):
        #os.system(r"touch {}".format(path))  # 调用系统命令行来创建文件

    r_file.seek(0)
    byte_index= 0
    #open
    while True:
        if byte_index != int(data_position):  # 判断是否在插入位置
            temp = r_file.read(1)  # 读出一个byte
            if len(temp) != 0:
                w_file.write(bytes(temp))#再写回去
                byte_index +=1
            else:
                 r_file.close()
                 w_file.close()
                 print(os.path.join(root, name)+"转档完成:)!!!")
                 break
        else:
            for i in random_list:
                a = struct.pack('B', i)
                w_file.write(a)
                byte_index += 1

if __name__ == '__main__':
    print("二进制文件插入工具V1.1.  作者：jiangbo lin")
    fileformat = input("请输入需要处理的文件格式,例如(bin):")
    fileformat = "."+ fileformat
    while True:
        data_position = input("请输入插入文件的位置(0~无穷):")
        if data_position.isdecimal():
            break
        else:
            print("输入位置信息非纯数字，请重新输入")

    while True:
        random_num = input("请输入随机数个数:")
        if random_num.isdecimal():
            '''
            index = 0
            while index < int(random_num):
                random_list.append(random.randint(0,255))
                index += 1
            index = 0
            for i in random_list:
                print(str(index) +":"+ hex(i) +" " + str(i) )
                index += 1
            '''
            break
        else:
            print("输入的随机个数非纯数字，请重新输入")
#**************************************************************************************
    filenumber = 0
    for root, dirs, files in os.walk(".", topdown=False):

        for name in files:
            if name.endswith(fileformat) :
                lenth = os.path.getsize(os.path.join(root, name))
                if int(data_position) >= lenth:
                    print("错误："+ name +"文件大小为"+str(lenth)+"byte,插入位置第"+str(data_position)+"Byte超过了此文件大小，此文件插入失败!!")
                else:
                    index = 0
                    random_list.clear()
                    while index < int(random_num):
                        random_list.append(random.randint(0, 255))#0~0xff
                        index += 1
                    index = 0
                    for i in random_list:
                        #print(str(index) + ":" + hex(i) + " " + str(i))
                        index += 1
                    con_files(root, name, data_position, random_list)
                filenumber += 1
    if filenumber ==0:
        print("!!!!!!!未找到*" + fileformat + "的相关文件，转档失败!!!!!!!")
    else:
        '''
        inf_file = open(os.path.join(root, "Information_file"), 'w+')
        messages = "(1)处理文件格式为:*" + str(fileformat)+'\n'
        inf_file.write(messages)

        messages = "(2)插入文件位置为: 第"+str(data_position)+"个Byte."'\n'
        inf_file.write(messages)
        messages = "(3)插入据个数为："+str(random_num)+"个"+'\n'
        inf_file.write(messages)
        messages = "(4)随机插入的数据为:" + '\n'
        inf_file.write(messages)
        index = 0
        for i in random_list:
            inf_file.write(str(index) + ":" + hex(i) + " " + str(i)+'\n')
            index += 1
        inf_file.close()
        '''
        time.sleep(3)

'''
    window = tk.Tk()
    var = tk.StringVar()
    # 第2步，给窗口的可视化起名字
    window.title('随机数据插入')
    # 第3步，设定窗口的大小(长 * 宽)
    window.geometry('500x300')  # 这里的乘是小x
    # 第4步，创建Lable
    tk.Label(window, text="File Path:").place(x=10, y=20)
    # 第5步，在图形界面上设定输入框控件entry并放置控件
    path = tk.StringVar()
    password = tk.Entry(window, textvariable=path, font=('Arial', 8))  # 显示成明文形式
    password.place(x=160, y=140)
    # 第6步，在图形界面上设定button
    userfile = tk.Button(window, text='SelectFile', command=selectpath)
    userfile.place(x=360, y=200)
    #password.bind("<Return>",lambda event:user_check(messageL,var_userpassword.get()))  # 注意这里是Return而不是Ente
    window.mainloop()
'''

