from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

browser = webdriver.Firefox()
browser.get("https://student.bodwell.edu/")
print(browser.title)

def logIN():
    userID = browser.find_element_by_id("userID")
    userID.send_keys("ding-han.yan@student.bodwell.edu")
    userPW = browser.find_element_by_id("userPW")
    userPW.send_keys("Sean0919")
    userLoginBtn = browser.find_element_by_id("userLoginBtn")
    userLoginBtn.click()

logIN()

sleep(5)

def getGrade():
    try:
        percentageGrade = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div[1]/div[2]/div/table/tbody/tr[1]/td[2]"))
        )
        print(percentageGrade.text)
    except:
        print("It didn't work")


getGrade()
