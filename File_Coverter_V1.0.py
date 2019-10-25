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
data_format = 0
bstr = []


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


def get_securty_data():
    input_time = 2
    while True:
        Security_data = input("输入加密的数据：")
        if Security_data.isdecimal():
            return int(Security_data)
        else:
            if input_time !=0:
                print("输入的非纯数字，您还有%d 机会" % input_time)
                input_time -= 1
            else:
                print("连续3次错误，2秒后自动退出!!!")
                time.sleep(2)
                exit()
def get_data_format():
    while True:
        format_data = input("请输人0(byte) 或 1(word)：")
        if format_data.isdecimal() and (int(format_data) == 0 or int(format_data) == 1):
            return int(format_data)
        else:
            print("输入的非纯数字，Byte = 0  word = 1")

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
if __name__ == '__main__':
    index = 0
    while True:
        #admin_pw = input("请输入管理员密码：")
        admin_pw = getpass.getpass("请输入密码：")
        if admin_pw == pw_123:
            #print("输入正确")
            break
        else:
            if try_time !=0:
                print("密码输入错误，您还有%d 机会" % try_time)
                try_time -= 1
            else:
                print("连续3次错误，2秒后自动退出!!!")
                time.sleep(2)
                exit()
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


