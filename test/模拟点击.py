#!/usr/bin/env python3 
# coding=utf-8

import subprocess
import time
# -*- coding: utf-8 -*-
# @file: test.py
# @author: xiaoxiao
# @date  : 2019/8/14

from PIL import Image
import os
import time

# 获取当前目录路径
path = os.path.abspath(os.path.dirname(__file__))

# 获取图片指定坐标点颜色值RGBA
def get_RGBA(image_path, pixelX, pixelY):
    '''
    :param image_path: a str, exp: /xxx/2019-08-14_17-26-01.png
    :param pixelX: int, exp: 280
    :param pixelY: int, exp: 650
    :return RGBA: a tuple, exp:(59, 201, 255, 255)
    '''
    img_src = Image.open(image_path)
    img_src = img_src.convert('RGBA')
    str_strlist = img_src.load()
    RGBA = str_strlist[pixelX, pixelY]
    img_src.close()
    return RGBA

# 获取手机屏幕截图，并保存在当前目录，文件名通过结合当前时间命名
def screen_shot():
    '''
    :return img_name: a str, exp: 2019-08-14_17-26-01.png
    '''
    img_name = str(time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time()))) + '.png'
    # 1.adb截图保存到手机/sdcard/目录
    cmd_screen_cap = 'adb shell screencap -p /sdcard/' + img_name
    os.popen(cmd_screen_cap)
    # 2.将手机截图pull到电脑当前目录
    while True:
        time.sleep(1)
        cmd_pull = 'adb pull /sdcard/' + img_name + ' ' + path + '/'
        os.popen(cmd_pull)
        try:
            Image.open(path + '/' + img_name) # 判断pull出来的图片是否能正常打开
            break # 如果打开正常整个，则跳出循环
        except: # 否则，图片打开异常的话，再次执行pull操作
            continue
    # 3.将手机截图从/sdcard/目录中删除
    cmd_delete_sdcard = 'adb shell rm -r /sdcard/' + img_name
    os.popen(cmd_delete_sdcard)
    return img_name


# 将RGBA转换成颜色16进制，这里也支持RGB的转换
def RGBA_to_Hex(RGBA):
    '''
    :param RGBA: a tuple, exp: (59, 201, 255, 255)
    :return hex_str: a str, exp: #3BC9FFFF
    '''
    hex_str = '#'
    for i in RGBA:
        num = int(i) # 将RGBA的数值转换成数字类型
        hex_str = hex_str + str(hex(num))[2:].replace('x', '0').upper()
    return hex_str


# 将颜色16进制转换成RGBA
def Hex_to_RGBA(hex_str):
    '''
    :param hex_str: a str, exp:#3BC9FFFF
    :return RGB or RGBA: a tuple, exp: (59, 201, 255, 255)
    '''
    r = str(int(hex_str[1:3], 16))
    g = str(int(hex_str[3:5], 16))
    b = str(int(hex_str[5:7], 16))
    temp_list = []
    if len(hex_str) == 9:
        a = str(int(hex_str[7:9], 16))
        rgba = r + ',' + g + ',' + b + ',' + a
        for s in rgba.split(','):
            temp_list.append(int(s)) # 逐个将RGBA保存到list中
        RGBA = tuple(temp_list) # 将list转成tuple
        return RGBA
    else:
        rgb = r + ',' + g + ',' + b
        for s in rgb.split(','):
            temp_list.append(int(s))
        RGB = tuple(temp_list)
        return RGB


def loop_click_for_android(run_time=30):
    inputs = str(input("请确保已打开测试页面(y/n)： "))
    start = subprocess.Popen("adb shell input tap 776 2163")
    time.sleep(0.11)
    start_buttun0 = subprocess.Popen("adb shell input swipe 918 1638 920 1063")
    # test = subprocess.Popen('adb devices', shell=True, stdout=subprocess.PIPE)
    popen = subprocess.Popen('adb shell getevent -l', shell=True, stdout=subprocess.PIPE)
    #popen.stdout.read()
    num = 0
    if inputs == "y":
        while True:
            resp = popen.stdout.readline() # 输出流
            # if resp:
            #     print(str(resp, encoding='utf-8'), num)
            if "SYN_REPORT" in str(resp, encoding='utf-8'):
                num += 1
                print(str(num) + str(resp, encoding='utf-8'))
            if "SYN_REPORT" in str(resp, encoding='utf-8') and num % 2 == 0:
                # if "SYN_REPORT" in str(resp, encoding='utf-8') and num % 2 == 1:
                #模拟点击确定
                start_buttun = subprocess.Popen("adb shell input tap 600 2086")
                time.sleep(0.19)
                #模拟点击下一题y
                start_buttun1 = subprocess.Popen("adb shell input tap 730 1718")
                time.sleep(0.05)
                #模拟滑动 adb shell input swipe 250 250 300 300
                start_buttun2 = subprocess.Popen("adb shell input swipe 917 1633 920 1063")
                # start_buttun = subprocess.Popen("adb shell input swipe 917 1633 920 1063")
                #num = 0
            # print(num)


if __name__ == "__main__":
    loop_click_for_android()
    # img_name = screen_shot()
    # img_path = path + '/' + img_name
    # print(img_path)
    # while not os.path.exists(img_name):
    #     time.sleep(1)
    # img_RGBA = get_RGBA(img_path, 280, 650)
    # print(img_RGBA)
    # img_hex = RGBA_to_Hex(img_RGBA)
    # print(img_hex)
