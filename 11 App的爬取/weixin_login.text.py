# _*_ coding:utf-8 _*_
__author__ = 'wang'
__date__ = '2018/6/26 16:40'

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

server = 'http://localhost:4723/wd/hub'

desired_caps = {
  "platformName": "Android",
  "deviceName": "Mi_Note_3",
  "appPackage": "com.tencent.mm",
  "appActivity": ".ui.LauncherUI"
}
# 设置server
driver = webdriver.Remote(server,desired_caps)

# 等待延时
wait = WebDriverWait(driver,30)

# 进入登录界面
login = wait.until(EC.presence_of_element_located((By.ID,'com.tencent.mm:id/d75')))
login.click()

# 点击输入手机号
phone = wait.until(EC.presence_of_element_located((By.ID,'com.tencent.mm:id/hz')))
phone.set_text(18840862253)

#点击下一步
next_step = wait.until(EC.element_to_be_clickable((By.ID,'com.tencent.mm:id/alr')))
next_step.click()

# 输入密码
password = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@resource-id="com.tencent.mm:id/hz"][1]')))
password.set_text('密码')

# 登录
login_click = wait.until(EC.element_to_be_clickable((By.ID,'com.tencent.mm:id/alr')))
login_click.click()

# 是否检测手机通讯录
ignore_phone_numbers = wait.until(EC.element_to_be_clickable((By.ID, 'com.tencent.mm:id/an2')))
ignore_phone_numbers.click()


