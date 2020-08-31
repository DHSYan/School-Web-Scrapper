from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from datetime import datetime
import threading
import os.path

browser = webdriver.Chrome()

def initialSetup():

    print("Welcome to BOGs WebScrapper")
    print("loading...")
    sleep(1)
    print("lets start by your email!")
    userEmail = input(": ")
    with open("userEmail.txt", "w") as STOREuserEmail:
        STOREuserEmail.write(userEmail)
        STOREuserEmail.close()
    print("loading...")
    sleep(1)
    print("Great!")
    sleep(1)
    print("Now the bodwell password, don't worry the creator of this program won't have access to your precious password.\n To find out more about your privacy, go to https://github.com/theTechyNerds/Bodwell-Web-Scraper ")
    userPassword = input(": ")
    with open("userPassword.txt", "w") as STOREuserPassword:
        STOREuserPassword.write(userPassword)
        STOREuserPassword.close()
    sleep(1)
    print("Loading...")

    with open("userEmail.txt", "r") as READuserEmail:
        print(READuserEmail.readline())
        READuserEmail.close()
    with open("userPassword.txt", "r") as READuserPassword:
        print(READuserPassword.readline())
        READuserPassword.close()
    print("Are these correct?")
    askIfCorrect = input(": ")

def changeInfo():
    print("What info do you want to change, Email or Password?")
    changeWhatKind = input(": ").upper()
    if changeWhatKind == "EMAIL":
        print("Enter you new Email")
        changeEmail = input(": ")
        with open("userEmail.txt", "w") as STOREuserEmail:
            STOREuserEmail.write(changeEmail)
            STOREuserEmail.close()
    elif changeWhatKind == "PASSWORD":
        print("Enter in your new password")
        changePassword = input(": ")
        with open("userPassword.txt", "w") as STOREuserPassword:
            STOREuserPassword.write(changePassword)
            STOREuserPassword.close()
def countingClock():
    threading.Timer(600.0, countingClock).start()
    print(datetime.today().strftime('%Y-%m-%d-%H:%M:%S'))

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
def login():
    with open("userEmail.txt", "r") as READuserEmail:
        loginEmail = READuserEmail.readline()
        READuserEmail.close()
    with open("userPassword.txt", "r") as READuserPassword:
        loginPassword = READuserPassword.readline()
        READuserPassword.close()

    userID = browser.find_element_by_id("userID")
    userID.send_keys(loginEmail)
    userPW = browser.find_element_by_id("userPW")
    userPW.send_keys(loginPassword)
    userLoginBtn = browser.find_element_by_id("userLoginBtn")
    userLoginBtn.click()
    sleep(5)
    submitHoursBtn = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[2]/button") #clicking the submit hours btn
    submitHoursBtn.click()
    closeSumbmitHoursBTN = browser.find_element_by_xpath("/html/body/div[3]/div/div/div/div[1]/button/span")
    closeSumbmitHoursBTN.click()
def submitHours():
    # if havePreset:
        # askIfHavePreset = input("You Have presets, would you like to use them?")
    print("Hello, to submit hours system")
    print("Enter Activity Name")
    enterActivityName = input(": ")
    selectCatergory = input('''
        (1) Physical, Outdoor & Recreation Education
        (2) Academic, Interest & Skill Development
        (3) Citizenship, Interaction & Leadership Experience
        (4) Arts, Culture & Local Exploration

        (1)(2)(3)(4): ''')
    print("Does this qualifies as Volunteer Hours?")
    qualifiesVolunteerHours = input(": ").upper()
    print("Location")
    askForLocation = input(": ")
    print("How many hours?")
    totalHourNumbers = input(": ")
    print("Who is the aprrover?")
    askForStaff = input(": ")
    print("The comments?")
    askForComment = input(': ')

    #ask for default staff at the begining of the program
    #based on the Activity name, have a template comment decirbe and event supervisor
    sleep(2)
    browser.refresh()
    sleep(10)
    try:
        submitHoursBtn = WebDriverWait(browser, 10).until(
            EC.presence_of_all_element_located((By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[2]/button"))
        ) #clicking the submit hours btn
        submitHoursBtn.click()
    except:
        print("Didn't see the submit btn")

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
    else:
        pass


    #try:
        #askForStaffDRP = WebDriverWait(browser, 10).until(Select(
            #EC.presence_of_element_located((By.XPATH, "//*[@id='sSubmit-approver']"))
        #))
        #if askForStaffDRP == "1": #can't get this to work need
            #askForStaffDRP.select_by_index(22)

    #except:
        #print("Can't choose a staff")

    #askForStaffDRP = Select(browser.find_element_by_xpath("//*[@id='sSubmit-approver']"))
    #if askForStaffDRP == "1":
        #askForStaffDRP.select_by_index(22)
    
    sendKeysComments = browser.find_element_by_xpath("//*[@id='sSubmit-comment1']")
    sendKeysComments.send_keys(askForComment)
def currentAccount():
    print("This is your currnet email:")
    with open("userEmail.txt", "r") as READuserEmail:
        print(READuserEmail.readline())
        READuserEmail.close()
    print("This is your currnet password:")
    with open("userPassword.txt", "r") as READuserPassword:
        print(READuserPassword.readline())
        READuserPassword.close()

countingClock()

checkEmailFile = (os.path.exists('userEmail.txt'))
checkPasswordFile = (os.path.exists('userPassword.txt'))
if checkEmailFile or checkPasswordFile  == False:
    initialSetup()
else:
    pass

browser.get("https://student.bodwell.edu/")
sleep(2)
url = browser.current_url
print(f"You are currently on: {url}")
login()

while True:
    print("'Help', with command")
    command = input("Command: ").upper()
    if command == "SUBMIT":
        submitHours()
    elif command == "GRADE":
        getGrade()
    elif command == "CHANGE":
        changeInfo()
    elif command == "CURRENT":
        currentAccount()
    elif command == "HELP":
        print('''
            "Submit" -- Submit Hours
            "Grade"  -- Get your currnet class grade
            "Change" -- Change your current Email and Password settings
            "Current" -- See your current email and password
        ''')
    elif command == "QUIT":
        print("Closing in 3")
        sleep(3)
        quit()