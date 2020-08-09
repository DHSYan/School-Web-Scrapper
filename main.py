from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from datetime import datetime
import threading

def countingClock():
    threading.Timer(60.0, countingClock).start()
    print(datetime.today().strftime('%Y-%m-%d-%H:%M:%S'))

countingClock()

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

sleep(10)

def submitHours():
    command = input("Would you like to submit hours?> ").upper()

    if command == "YES":
        enterActivityName = input("Ener Activity Name: ")
        selectCatergory = input('''
            (1) Physical, Outdoor & Recreation Education
            (2) Academic, Interest & Skill Development
            (3) Citizenship, Interaction & Leadership Experience
            (4) Arts, Culture & Local Exploration
        ''')
        qualifiesVolunteerHours = input("Does this qualifies as Volunteer Hours?> ")
        askForLocation = input("Location: ")
        startDate = input("Start date: ")
        endDate = input("End date: ")
        totalHourNumbers = input("Total Hours: ")
        
        #ask for default staff at the begining of the program
        #based on the Activity name, have a template comment decirbe and event supervisor

        submitHoursBtn = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[2]/button")
        submitHoursBtn.click()

        sleep(10)

        try:
            activityName = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="sSubmit-actName"]'))
            )
            activityName.send_keys(enterActivityName)

        except:
            print("Something is wrong")
        
    else:
        pass
       
submitHours()
        
def getGrade():
    try:
        percentageGrade = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div[1]/div[2]/div/table/tbody/tr[1]/td[2]"))
        )
        print(datetime.today().strftime('%Y-%m-%d-%H:%M:%S')+ " " + percentageGrade.text)

        with open("grades.txt", "a") as writeGrades:
            writeGrades.write(datetime.today().strftime('%Y-%m-%d-%H:%M:%S') + " " +percentageGrade.text +"\n")

            writeGrades.close()
        
    except:
        print("It didn't work")


getGrade()



