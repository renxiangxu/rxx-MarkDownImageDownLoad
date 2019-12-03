#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re
import requests
import os
import io
import time
import sys
import imghdr
import urllib3
import Tkinter as tk  # 使用Tkinter前需要先导入
from tkFileDialog import *

# 输入文件夹，需要修改路径为简书打包下载后解压出的文件夹
INPUT_DIR = '这里替换成你的文件路径'

# 输出文件夹，不需要修改，默认为根路径下的output_images文件夹，不然文章的链接会定位不到
OUTPUT_DIR = INPUT_DIR + '/output_images'

pool_manager = urllib3.PoolManager()

def ensure_dir_exist(dir_name):
    if not os.path.exists(dir_name):
        print("{} 不存在，创建它。".format(dir_name))
        os.mkdir(dir_name)
    else:
        print("{} 存在，无需新创建。".format(dir_name))

def start_a_file(a_markdown_file, output_dir):
    f = open(a_markdown_file)
    line = f.readline()
    i = 0
    while 1:
        line = f.readline()
        if not line:
            break
        i = i + 1
        ln = line[:-1]
        # print("[{}] [{}]".format(i, ln))
        process_line(ln, output_dir, a_markdown_file)
    f.close()
    return


def process_line(line, output_dir, a_markdown_file):
    if line == '':
        return
    img_list = re.findall(r"\!\[[^\]]*\]\((.+?)\)", line, re.S)
    for iu in img_list:
        print "-------------"
        img_url = iu.split('?')[0]

        oldName = iu.split(' ')[0]
        print "img_url:::::" + img_url
        print "oldName:::::" + oldName
        print('[Process:]' + img_url)

        if img_url.startswith(('http://', 'https://')):
            suffix = download_image_file(img_url, output_dir)
            #替换原来的链接
            print "a_markdown_file:::::" + a_markdown_file
            title =  a_markdown_file.rsplit('/',1)[1]
            title = title.split(".")[0]
            print "title:::::" + title
            new_name = "output_images" + "/"  + os.path.basename(img_url)
            print "new_name:::::" + new_name
            print "img_url:::::" + img_url
            print "----------------"
            # print "路径6666= " + output_dir
            # print "路径7777= " + new_name
            modify_md_content(a_markdown_file,new_name ,oldName, suffix) 
        else:
            print("[ 不合法的 image url]:" + img_url)
    return

def modify_md_content(a_markdown_file, img_local_path, img_url, suffix):

    md_file_path = a_markdown_file 
    copy_md_file_path = a_markdown_file + "_copy" +"md"

    # 打开md文件然后进行替换
    with io.open(md_file_path, 'r', encoding='utf-8') as fr:
        with io.open(copy_md_file_path, 'w', encoding='utf-8') as fw:
            data = fr.read()
            # data = re.sub('\(/配图/', '(配图/', data)
            # data = re.sub('<br>', '<br>\n', data)
            # data = re.sub('<br>', '', data)
            print "替换::::::" + img_url
            print "替换2::::::" + img_local_path
            img_local_path = "../" + img_local_path + "." + suffix
            # data = re.sub(img_url, img_local_path, data)
            data = data.replace(img_url, img_local_path)

            fw.write(data)  # 新文件一次性写入原文件内容
            # fw.flush()

        # 删除原文件
        os.remove(md_file_path)
        # 重命名新文件名为原文件名
        os.rename(copy_md_file_path, md_file_path)
        # print(f'{md_file_path} done...')
        time.sleep(0.5)

def download_image_file(url, output_dir):
    print(" # 准备下载")
    r = requests.get(url)
    response = pool_manager.urlopen('GET', url)
    img = r.content
    print(" # 准备写入")
    suffix = imghdr.what(None, response.data);
    if imghdr.what(None, response.data) is None:
        suffix = "jpeg"
    new_name = output_dir + "/" + os.path.basename(url) + "." + suffix
    with open(new_name, 'wb') as f:
        f.write(img)
        print(" # 写入DONE")
    return suffix

def walk_dir(dir_name):
    for root, dirs, files in os.walk(dir_name):
        relative_name = root.replace(INPUT_DIR, '')
        print('  root={}'.format(relative_name))
        ensure_dir_exist(OUTPUT_DIR + "/" + relative_name)
        for f in files:
            print('   file = {}'.format(f))
            if f.split('.')[-1] != 'md':
                continue
            a_markdown_file = os.path.join(root, f)
            # 生成图片存放的文件夹。
            dir_name = (a_markdown_file.split('/')[-1]).split('.')[0]

            #原本是根据文章生成目录，但是文章名有中文，就直接丢到同一个文件夹里面去
            # this_file_output_dir = OUTPUT_DIR + '/' + relative_name + '/' + dir_name
            this_file_output_dir = OUTPUT_DIR + '/' 

            print('   this_file_output_dir = {}'.format(this_file_output_dir))
            ensure_dir_exist(this_file_output_dir)
            # 处理文件
            start_a_file(a_markdown_file, this_file_output_dir)
    global workState
    workState = 0

# filePath = INPUT_DIR + fileName
# print('filePath={}'.format(filePath))


window = tk.Tk()
window.title('RxxMarkDown文件图片替换-目前只支持简书')
window.geometry('500x300')

fileDirEntryText = tk.StringVar()
fileDirEntryText.set('选择文件路径')
fileDirEntry = tk.Entry(window, textvariable=fileDirEntryText, font=('Arial', 14))
#entry_usr_name.place(x=120,y=175)
fileDirEntry.pack()

fileDirEntry.delete(0, tk.END)  # 将输入框里面的内容清空
fileDirEntry.insert(0, '选择文件路径')
filepath = tk.StringVar()
def filefound():
    filepath= askdirectory()
    print filepath
    fileDirEntry.delete(0, tk.END)  # 将输入框里面的内容清空
    fileDirEntry.insert(0, filepath)
findFileText = tk.StringVar(master=None, value="设置文件夹", name=None)
chooseButton = tk.Button(master=window,textvariable = findFileText, font=('Arial', 14), width=10, height=1, command=filefound)
chooseButton.pack()

def startDef():
    global INPUT_DIR
    INPUT_DIR = fileDirEntry.get()
    print "INPUT_DIR" + INPUT_DIR
    global OUTPUT_DIR
    OUTPUT_DIR = INPUT_DIR + '/output_images'
    print "OUTPUT_DIR" + OUTPUT_DIR
    global workState
    if workState == 0:
        #workState = 1
        ensure_dir_exist(OUTPUT_DIR)
        walk_dir(INPUT_DIR)
    
workState = 0

okButton = tk.Button(window, textvariable = tk.StringVar(value="确定"), font=('Arial', 14),width=10, height=1, command = startDef)
okButton.pack()


reload(sys) 
sys.setdefaultencoding('utf8')
window.mainloop()

