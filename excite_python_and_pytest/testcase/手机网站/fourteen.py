"""
# @Time : 2022-02-07 15:48 

# @Author : sarah

# @File : fourteen.py 

# @Software: PyCharm
"""
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


driver = webdriver.Chrome()


driver.get("https://uat.cdcc.cmbchina.com/stage-express/bill-stage-integration")
        # self.driver.set_window_size(974, 1080)
        # self.driver.find_element(By.CSS_SELECTOR, "input").click()
        # self.driver.find_element(By.CSS_SELECTOR, "input").send_keys("533528202201018107")
        # self.driver.find_element(By.CSS_SELECTOR, ".placeholder-msg_RN9zV").click()


driver.quit()

