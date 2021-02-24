# encoding=utf-8
import subprocess
import time

def library_loop_click():
    fling_0 = subprocess.Popen("adb shell input swipe 785 1593 47 1593")
    time.sleep(1)
    start_buttun = subprocess.Popen("adb shell input tap 901 1700")
    time.sleep(3)
    fling_1 = subprocess.Popen("adb shell input swipe 550 547 550 2016")
    time.sleep(1)
    # 超星读书
    start_buttun = subprocess.Popen("adb shell input tap 180 1056")
    time.sleep(2)
    start_buttun = subprocess.Popen("adb shell input tap 945 2332")
    time.sleep(1)
    start_buttun = subprocess.Popen("adb shell input tap 886 550")
    time.sleep(2)
    # 当日任务
    book_loop_click()
    listen_loop_click()
    magazine_loop_click()
    pic_loop_click()

def book_loop_click():
    pass

def listen_loop_click():
    pass

def magazine_loop_click():
    pass

def pic_loop_click():
    pass

if __name__ == "__main__":
    library_loop_click()
