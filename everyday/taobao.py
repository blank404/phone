#!/usr/bin/env python3 
# coding=utf-8

import uiautomator2 as u2
import time

d = u2.connect('192.168.0.102')
if d.info:
    print("connect right")

# 打开淘宝
# d.app_start("com.meizu.mzbbs")
if d(text="手机淘宝").exists:
    d(text="手机淘宝").click()
print("taobao open right")

# 红包签到
while not d(description="红包签到").exists:
    time.sleep(1)
d(description="红包签到").click()
time.sleep(1)
print("红包签到完成")
d.click(0.085, 0.084)  # 点击返回主界面
time.sleep(1)

# 芭芭农场

# 小黑盒
sx, sy, ex, ey = 0.894, 0.217, 0.117, 0.213
while not d(description="小黑盒").exists:
    d.swipe(sx, sy, ex, ey)
d(description="小黑盒").click()
print("小黑盒已打开")
time.sleep(1)
d.click(0.64, 0.354)  # 点击开盒有喜
print("开盒有喜已打开")
time.sleep(2)
while d(text="去完成").exists:
    if d(description="去完成").exists:
        d(description="去完成").click()
    # 1
    if d(description="确认兑换").exists:
        d(description="确认兑换").click()
    # 2
    time.sleep(11)
    d(description="转到上一层级").click()
    time.sleep(1)
    d.click(0.817, 0.398)  # 点我开盒
    time.sleep(10.5)
    




