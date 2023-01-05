from time import sleep
from selenium import webdriver
import yagmail
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import warnings
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

fromaddr = 'your gmail usernam'
app_password = 'your gmail token' #https://towardsdatascience.com/automate-sending-emails-with-gmail-in-python-449cc0c3c317
to = 'receiver1@gmail.com'

def sendEmail_ok():
    subject = 'Visa Booking'
    content = ["Your Appointment is Ready", 'booked.png']
    try:
        with yagmail.SMTP(fromaddr, app_password) as yag:
            yag.send(to, subject, content)
            print('Sent email successfully')
        sleep(3)
    except:
        print("\nFailed to send email, try again.")

def sendEmail_nok():
    subject = 'Error E-Mail'
    content = ["You can find an image file attached.", 'unexpected_error.png']
    try:
        with yagmail.SMTP(fromaddr, app_password) as yag:
            yag.send(to, subject, content)
            print('Sent email successfully')
        sleep(3)
    except:
        print("\nFailed to send email, try again.")

def checkAvailability():
    print("\nChecking Availability...")
    site = "https://www.vfsvisaonline.com/Netherlands-Global-Online-Appointment_Zone2/AppScheduling/AppWelcome.aspx?P=%2FiOLWQz9Vk07YwT57Xup3WWpcMKp4QcG2ApaJBrIfls%3D"

    warnings.filterwarnings("ignore")
    chrome_options = Options()
    chrome_options.add_argument('--window-size=1920,1080')
    #chrome_options.headless = True

    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
    driver.get(site)

    try:
        appointment = driver.find_element(By.ID, "plhMain_lnkSchApp")
        appointment.click()
        Select(driver.find_element(By.ID, "plhMain_cboVAC")).select_by_index(2)
        driver.find_element(By.ID, "plhMain_btnSubmit").click()

        person = driver.find_element(By.ID, "plhMain_tbxNumOfApplicants")
        person.send_keys(Keys.BACKSPACE)
        person.send_keys("2")

        Select(driver.find_element(By.ID, "plhMain_cboVisaCategory")).select_by_index(6)
        driver.find_element(By.ID, "plhMain_btnSubmit").click()

        while("No date(s)" in driver.page_source):
            print(f"\nTrying Again")
            driver.refresh()

        sleep(2)
        Select(driver.find_element(By.ID, "plhMain_repAppVisaDetails_cboTitle_0")).select_by_index(1)
        sleep(2)
        driver.find_element(By.NAME, "ctl00$plhMain$repAppVisaDetails$ctl01$tbxFName").send_keys('FIRSTNAME1')
        sleep(2)
        driver.find_element(By.NAME, "ctl00$plhMain$repAppVisaDetails$ctl01$tbxLName").send_keys('SURNAME1')
        sleep(2)
        driver.find_element(By.NAME, "ctl00$plhMain$repAppVisaDetails$ctl01$tbxContactNumber").send_keys('PHONE NUMBER1')
        sleep(2)
        driver.find_element(By.NAME, "ctl00$plhMain$repAppVisaDetails$ctl01$tbxEmailAddress").send_keys('username1@gmail.com')
        sleep(2)

        Select(driver.find_element(By.ID, "plhMain_repAppVisaDetails_cboTitle_1")).select_by_index(2)
        sleep(2)
        driver.find_element(By.NAME, "ctl00$plhMain$repAppVisaDetails$ctl02$tbxFName").send_keys('FIRSTNAME2')
        sleep(2)
        driver.find_element(By.NAME, "ctl00$plhMain$repAppVisaDetails$ctl02$tbxLName").send_keys('SURNAME2')
        sleep(2)
        driver.find_element(By.NAME, "ctl00$plhMain$repAppVisaDetails$ctl02$tbxContactNumber").send_keys('PHONE NUMBER2')
        sleep(2)
        driver.find_element(By.NAME, "ctl00$plhMain$repAppVisaDetails$ctl02$tbxEmailAddress").send_keys('username2@gmail.com')
        sleep(2)

        Select(driver.find_element(By.ID, "plhMain_cboConfirmation")).select_by_index(1)
        sleep(2)
        driver.find_element(By.ID, "plhMain_btnSubmit").click()
        sleep(30)

        while(True):
            driver.find_element(By.XPATH, "//*[@id='plhMain_cldAppointment']/tbody/tr[1]/td/table/tbody/tr/td[3]/a").click()

            if ("Error in the application, please contact admin." in driver.page_source):
                print(f"\nReturns Error in June.")

            elif ("No date(s) available for current month." in driver.page_source):
                print(f"\nNo Appointments in June.")

            elif ("Appointments are" in driver.page_source):
                print("\nAvailable in June\n")
                sleep(5)
                driver.find_element(By.CLASS_NAME, "OpenDateAllocated").click()
                sleep(2)
                driver.find_element(By.ID, "plhMain_gvSlot_lnkTimeSlot_0").click()
                sleep(2)
                driver.switch_to.alert.accept()
                sleep(10)
                driver.save_screenshot('booked.png')
                sleep(10)
                sendEmail_ok()
                sleep(10)

            else:
                print("Unexpected Error")
                driver.save_screenshot('unexpected_error.png')
                sleep(10)
                sendEmail_nok()
                sleep(10)

            driver.find_element(By.XPATH, "//*[@id='plhMain_cldAppointment']/tbody/tr[1]/td/table/tbody/tr/td[1]/a").click()

            if ("Error in the application, please contact admin." in driver.page_source):
                print(f"\nReturns Error in May.")

            elif ("No date(s) available for current month." in driver.page_source):
                print(f"\nNo Appointments in May.")

            elif ("Appointments are" in driver.page_source):
                print("\nAvailable in May\n")
                sleep(5)
                driver.find_element(By.CLASS_NAME, "OpenDateAllocated").click()
                sleep(2)
                driver.find_element(By.ID, "plhMain_gvSlot_lnkTimeSlot_0").click()
                sleep(2)
                driver.switch_to.alert.accept()
                sleep(10)
                driver.save_screenshot('booked.png')
                sleep(10)
                sendEmail_ok()
                sleep(10)

            else:
                print("Unexpected Error")
                driver.save_screenshot('unexpected_error.png')
                sleep(10)
                sendEmail_nok()
                sleep(10)

    finally:
        driver.quit()

checkAvailability()
