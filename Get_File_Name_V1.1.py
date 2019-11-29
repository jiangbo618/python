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
test = []
path_list = {}
try_time = 2
index = 0
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
    #print("**************作者:Jiangbo Lin****版本V1.3**********")
    name_list = open('SONG.LST', 'w')  #
    code_list = open('song.h', 'w')  #
    for root, dirs, files in os.walk(".", topdown=False):
        #print(dirs)
        for name in files:
                if      name.endswith(".f1a") or  name.endswith(".b") \
                        or name.endswith(".a")  or name.endswith(".d")\
                        or name.endswith(".sp4") or name.endswith(".sp5") or name.endswith(".rav") \
                        or name.endswith(".a16") or name.endswith(".a18") or name.endswith(".a34") \
                        or name.endswith(".F1A") or name.endswith(".B") \
                        or name.endswith(".A") or name.endswith(".D") \
                        or name.endswith(".SP4") or name.endswith(".SP5") or name.endswith(".RAV") \
                        or name.endswith(".A16") or name.endswith(".A18") or name.endswith(".A34") \
                        or name.endswith(".mid")or name.endswith(".MID"):
                                #print(root)
                    #con_file(os.path.join(root, name),root,name)
                    if root.endswith("song") or root.endswith("SONG"):#限制了查找的文件夹名字
                        print(str(index) +" " + name )
                        songname  = name
                        #name_list.write(name + "\n")
                        test = name.split(".")
                        #test = test[0]
                        code_list.write("#define "+ test[0] +" " +str(index)+"\n")
                        name_list.write(songname + "\n")
                        index += 1
                    #print("{0}转换完成".format(os.path.join(root, name)))
    name_list.close()
    code_list.close()
    print("文件提取完成，总共：" + str(index)+" 个文件提取完成！")
    print("**************作者:Jiangbo Lin 软件版本V1.3**********")
    time.sleep(2)

