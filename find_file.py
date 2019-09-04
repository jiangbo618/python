#!/usr/bin/evn python
# encoding: utf-8
# @version     : python 3.7
# @Time        :2019/9/4 11:31
# @Author      :Jiangbo Lin
# @Filename    :find_file.py 
# @Description :

import os

for root, dirs, files in os.walk("c:\\", topdown=True):
    print("***********************\n")
    print(root)  # 是一个string，代表目录的路径
    print(dirs)  # 是一个list，包含了dirpath下所有子目录的名字
    print(files) # 包含了非目录文件的名字
    for name in files:
        if os.path.join(root, name).endswith(".jpg"):
            print(os.path.join(root, name))
