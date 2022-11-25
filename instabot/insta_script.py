from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

PATH = "C:\Program Files (x86)/chromedriver.exe"

url = "https://services.mpcz.in/Consumer/#/ViewPayBillApp/bill-Payment"
web = webdriver.Chrome(PATH)
web.get(url)

# time.sleep(15)
ivrs_number = "N2445015656"
ivrs_box = web.find_element(By.XPATH,"//*[@id='mat-input-0']")
ivrs_box.send_keys(ivrs_number)

web.find_element(By.XPATH,"//*[@id='mat-select-0']").click()
web.find_element(By.XPATH,"//*[@id='mat-option-0']").click()
web.find_element(By.XPATH,"//*[@id='payForm']/mat-card/mat-card-content/div[2]/div[2]/div/mat-card-actions/button[1]/span").click()
# bill = web.find_element(By.XPATH,"//*[@id='billDetail']/td[6]").text
# print(bill)
