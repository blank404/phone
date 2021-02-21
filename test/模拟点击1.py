#!/usr/bin/env python3 
# coding=utf-8

import subprocess
import time

def loop_click_for_android(run_time=30):
    #inputs = str(input("请确保已打开测试页面(y/n)： "))
    #start = subprocess.Popen("adb shell input tap 513 1790")
    #time.sleep(0.1)
    # test = subprocess.Popen('adb devices', shell=True, stdout=subprocess.PIPE)
    popen = subprocess.Popen('adb shell getevent -l', shell=True, stdout=subprocess.PIPE)
    #popen.stdout.read()
    num = 0
    #if inputs == "y":
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
            start_buttun = subprocess.Popen("adb shell input tap 545 1781")
            #模拟点击下一题y
            start_buttun1 = subprocess.Popen("adb shell input tap 527 1746")
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
