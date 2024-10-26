
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sched
import time
import pyautogui

# 初始化sched模块的调度器
scheduler = sched.scheduler(time.time, time.sleep)

# 定义一个函数，用于执行点击操作
def automate_click():
    # 假设飞书应用的按钮在屏幕上的位置是(100, 200)
    button_position = (100, 200)
    # 移动鼠标到指定位置
    pyautogui.moveTo(button_position)
    # 执行点击操作
    pyautogui.click()

# 定义一个函数，用于设置定时任务
def setup_schedule(delay, action):
    # 在指定的延迟之后，执行提供的action
    scheduler.enter(delay, 1, action)

# 定义一个函数，用于获取坐标任务
def get_mouse_position():
    try:
        while True:
            # 打印鼠标当前位置
            print(pyautogui.position())
            # 暂停一秒钟方便观察
            time.sleep(1)
    except KeyboardInterrupt:
        # 如果有键盘中断（如Ctrl+C），则退出循环
        print("位置获取结束")

if __name__ == '__main__' :
    # 在5秒后执行自动点击
    setup_schedule(5, automate_click)
    # 运行调度器
    scheduler.run()
    # 鼠标触发
    get_mouse_position()