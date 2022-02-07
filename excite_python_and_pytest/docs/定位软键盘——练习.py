"""
# @Time : 2022-02-07 17:27 

# @Author : sarah

# @File : 定位软键盘.py 

# @Software: PyCharm
"""
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://uat.cdcc.cmbchina.com")
time.sleep(3)
f=driver.find_element_by_css_selector("iframe#fQRLGIN")##fQRLGIN
driver.switch_to.frame(f)
driver.find_element_by_id("USERID").send_keys("123456")
driver.find_element_by_id("keyboardBtn").click()
keybordkey=driver.find_element_by_id("keybordkeyboardBtn") #软键盘
table=keybordkey.find_element_by_tag_name("table")
row=table.find_elements_by_tag_name("tr")

for i in range(len(row)):
    row[i].find_elements_by_tag_name("td")[2].click()