# _*_ coding:utf-8 _*_
__author__ = 'wang'
__date__ = '2018/6/26 17:38'

import time
import re

from pymongo import MongoClient
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException



# 驱动配置
PLATFORM = "Android"
DEVICE_NAME = "Mi_Note_3"
APP_PACKAGE = "com.tencent.mm"
APP_ACTIVITY = ".ui.LauncherUI"
DRIVER_SERVER = 'http://localhost:4723/wd/hub'
TIMEOUT = 300

# 数据库配置
MONGO_URL = 'localhost'
MONGO_DB = 'moments'
MONGO_COLLECTION = 'moments'

# 账号与密码
USER_NAME = 账号
PASSWORD = 密码

# 滑动点
FLICK_START_X = 300
FLICK_START_Y =300
FLICK_DISTANCE = 700

SCROLL_SLEEP_TIME = 1


class Moments():
    def __init__(self):
        """
        初始化
        """

        # 配置驱动
        self.desired_caps = {
            "platformName": PLATFORM,
            "deviceName": DEVICE_NAME,
            "appPackage": APP_PACKAGE,
            "appActivity": APP_ACTIVITY,
        }

        self.driver = webdriver.Remote(DRIVER_SERVER,self.desired_caps)
        self.wait = WebDriverWait(self.driver,TIMEOUT)
        self.client = MongoClient(MONGO_URL)
        self.db = self.client[MONGO_DB]
        self.collection = self.db[MONGO_COLLECTION]

    def login(self):
        # 登录按钮
        login = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/d75')))
        login.click()

        # # 手机输入
        # phone = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/hz')))
        # phone.set_text(USER_NAME)
        #
        # # 下一步
        # next_step = self.wait.until(EC.element_to_be_clickable((By.ID, 'com.tencent.mm:id/alr')))
        # next_step.click()
        #
        # # 输入密码
        # password = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@resource-id="com.tencent.mm:id/hz"][1]')))
        # password.set_text(PASSWORD)

        # 用QQ登录
        change_login_qq = self.wait.until(EC.element_to_be_clickable((By.ID,'com.tencent.mm:id/c1t')))
        change_login_qq.click()
        username = self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@resource-id="com.tencent.mm:id/hz"][1]')))
        username.set_text(账号)
        password = self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@resource-id="com.tencent.mm:id/c1s"]//*[@resource-id="com.tencent.mm:id/hz"]')))
        password.set_text('密码')

        # 登录
        login_click = self.wait.until(EC.element_to_be_clickable((By.ID, 'com.tencent.mm:id/c1u')))
        login_click.click()

        # 是否检测手机通讯录
        ignore_phone_numbers = self.wait.until(EC.element_to_be_clickable((By.ID,"com.tencent.mm:id/an2")))
        ignore_phone_numbers.click()

    def enter(self):
        # 选项卡
        print('enter')
        driver = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME,'android.widget.RelativeLayout')))
        TouchAction(driver).tap(x=654, y=1803).perform()
        # tab = self.wait.until(
        #     EC.presence_of_element_located((By.XPATH, '//*[@resource-id="com.tencent.mm:id/b0w"][3]')))
        # tab.click()
        print('end')
        # 朋友圈
        moments = self.wait.until(EC.presence_of_element_located((By.ID,'com.tencent.mm:id/a7f')))
        moments.click()

    def crawl(self):
        while True:

            # 当前页面显示的所有状态
            items = self.wait.until(EC.presence_of_all_elements_located((By.XPATH,'//*[@resource-id="com.tencent.mm:id/dja"]//android.widget.Framelayout')))

            # 上滑
            self.driver.swipe(FLICK_START_X, FLICK_START_Y + FLICK_DISTANCE, FLICK_START_Y, FLICK_START_Y)

            # 遍历每条状态
            for item in items:
                try:
                    # 昵称
                    nickname = item.find_element_by_id('com.tencent.mm:id/as6').get_attribute('text')

                    # 正文
                    content = item.find_element_by_id('com.tencent.mm:id/dkf').get_attribute('text')

                    # 日期
                    date = item.find_element_by_id('com.tencent.mm:id/dfw').get_attribte('text')

                    # 处理日期
                    date = self.date(date)

                    data = {
                        'nickname':nickname,
                        'content':content,
                        'date':date,
                    }

                    # 插入MongoDB
                    self.collection.update({'nickname': nickname, 'content': content}, {'$set': data}, True)
                    time.sleep(SCROLL_SLEEP_TIME)
                except NoSuchElementException:
                    pass

    def date(self,datetime):
        """
        处理时间
        :param datetime: 原始时间
        :return: 处理后时间
        """

        # 分钟
        if re.match('\d+分钟前',datetime):
            minute = re.match('(\d+)',datetime).group(1)
            datetime = time.strftime('%Y-%m-%d',time.localtime(time.time() - float(minute) * 60))

        # 小时
        if re.match('\d+小时前',datetime):
            hour = re.match('(\d+)',datetime).group(1)
            datetime = time.strftime('%Y-%m-%d',time.localtime(time.time() - float(hour) * 60 * 60))

        # 昨天
        if re.match('昨天',datetime):
            datetime = time.strftime('%Y-%m-%d',time.localtime(time.time() - 24 * 60 * 60))

        # 几天前
        if re.match('\d分钟前',datetime):
            day = re.match('(\d+)',datetime).group(1)
            datetime = time.strftime('%Y-%m-%d',time.localtime(time.time() - float(day) * 60))

        return datetime

    def main(self):
        self.login()
        print('11')
        time.sleep(10)
        self.enter()
        print('1212')
        self.crawl()


if __name__ == '__main__':
    moment = Moments()
    moment.main()