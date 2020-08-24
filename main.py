from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from datetime import datetime
import threading

def countingClock():
    threading.Timer(600.0, countingClock).start()
    print(datetime.today().strftime('%Y-%m-%d-%H:%M:%S'))

countingClock()

browser = webdriver.Chrome()
browser.get("https://student.bodwell.edu/")
sleep(3)
url = browser.current_url
print(f"You are currently on: {url}")

def logIN():
    userID = browser.find_element_by_id("userID")
    userID.send_keys("ding-han.yan@student.bodwell.edu")
    userPW = browser.find_element_by_id("userPW")
    userPW.send_keys("Sean0919")
    userLoginBtn = browser.find_element_by_id("userLoginBtn")
    userLoginBtn.click()
    sleep(5)
    submitHoursBtn = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[2]/button") #clicking the submit hours btn
    submitHoursBtn.click()
    closeSumbmitHoursBTN = browser.find_element_by_xpath("/html/body/div[3]/div/div/div/div[1]/button/span")
    closeSumbmitHoursBTN.click()

    

logIN()

#sleep(7)

def submitHours():
    command = input("Would you like to submit hours?> ").upper()

    if command == "YES":
        enterActivityName = input("Ener Activity Name: ")
        selectCatergory = input('''
            (1) Physical, Outdoor & Recreation Education
            (2) Academic, Interest & Skill Development
            (3) Citizenship, Interaction & Leadership Experience
            (4) Arts, Culture & Local Exploration

            (1)(2)(3)(4): ''')
        qualifiesVolunteerHours = input("Does this qualifies as Volunteer Hours?> ").upper()
        askForLocation = input("Location: ")
        totalHourNumbers = input("Total Hours: ")
        askForStaff = input("Approver?> ")
        askForComment = input('Comments: ')

        
        #ask for default staff at the begining of the program
        #based on the Activity name, have a template comment decirbe and event supervisor

        browser.refresh()
        submitHoursBtn = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[2]/button") #clicking the submit hours btn
        submitHoursBtn.click()

        try:
            activityName = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="sSubmit-actName"]'))
            )
            activityName.send_keys(enterActivityName)

        except:
            print("Something is wrong")
        
        activityCatergroydrp = Select(browser.find_element_by_id("sSubmit-actCategory")) #Drop Box
        if selectCatergory == "1":
            activityCatergroydrp.select_by_index(1)
        elif selectCatergory == "2":
            activityCatergroydrp.select_by_index(2)
        elif selectCatergory == "3":
            activityCatergroydrp.select_by_index(3)
        elif selectCatergory == "4":
            activityCatergroydrp.select_by_index(4)
        else:
            print("You didn't Choose a option, try again")
        
        if qualifiesVolunteerHours == "YES": #tyring to find out if qualifies as Vol Hours
            volHoursBtnYES = browser.find_element_by_xpath("/html/body/div[3]/div/div/div/div[2]/div[1]/form/div[3]/div/div[1]/label")
            volHoursBtnYES.click()
        elif qualifiesVolunteerHours == "NO":
            volHoursBtnNO = browser.find_element_by_xpath("/html/body/div[3]/div/div/div/div[2]/div[1]/form/div[3]/div/div[2]/label")
            volHoursBtnNO.click()
        else:
            print("You didn't specify if this qualifies")

        locationSendKeys = browser.find_element_by_xpath("//*[@id='sSubmit-location']")
        locationSendKeys.send_keys(askForLocation)

        datepicker = browser.find_element_by_xpath("//*[@id='sSubmit-sDate']")
        datepicker.click()
        #for options in browser.find_element_by_class("bootstrap-datetimepicker-widget dropdown-menu usetwentyfour top open"):
            #if options.text == "1":
               # options.click()
                #break
        endDateBox = browser.find_element_by_xpath("//*[@id='sSubmit-eDate']")
        endDateBox.click()

        numberOfHoursDRP = Select(browser.find_element_by_xpath("//*[@id='sSubmit-hours']"))
        if totalHourNumbers == "1":
            numberOfHoursDRP.select_by_index(2)
        elif totalHourNumbers == "2":
            numberOfHoursDRP.select_by_index(4)


        try:
            askForStaffDRP = WebDriverWait(browser, 10).until(Select(
                EC.presence_of_element_located((By.XPATH, "//*[@id='sSubmit-approver']"))
            ))
            if askForStaffDRP == "1": #can't get this to work need
                askForStaffDRP.select_by_index(22)

        except:
            print("Can't choose a staff")

        #askForStaffDRP = Select(browser.find_element_by_xpath("//*[@id='sSubmit-approver']"))
        #if askForStaffDRP == "1":
            #askForStaffDRP.select_by_index(22)
        
        sendKeysComments = browser.find_element_by_xpath("//*[@id='sSubmit-comment1']")
        sendKeysComments.send_keys(askForComment)

 

        
        


    else:
        pass
       
submitHours()
        
def getGrade():

    sleep(5)

    try:
        percentageGradeEnglish = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div[1]/div[2]/div/table/tbody/tr[1]/td[2]"))
        )
        print(datetime.today().strftime('%Y-%m-%d-%H:%M:%S')+ " English = " + percentageGradeEnglish.text)

        with open("grades.txt", "a") as writeGrades:
            writeGrades.write(datetime.today().strftime('%Y-%m-%d-%H:%M:%S') + " English =  " + percentageGradeEnglish.text +"\n")
            writeGrades.close()
        
    except:
        print("It didn't work")

    try:
        percentageGradeScience = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[2]/div[1]/div[2]/div/table/tbody/tr[2]/td[2]" ))
        )
        print(datetime.today().strftime('%Y-%m-%d-%H:%M:%S')+ " Science = " + percentageGradeScience.text)

        with open("grades.txt", "a") as writeGrades:
            writeGrades.write(datetime.today().strftime('%Y-%m-%d-%H:%M:%S') + " Science = " + percentageGradeScience.text +"\n")
            writeGrades.close()
        
    except:
        print("It didn't work")


#getGrade()



