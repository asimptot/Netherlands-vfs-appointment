import time
from selenium import webdriver
from mailthon import postman, email
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import warnings
from selenium.webdriver.common.keys import Keys

while True:
    fromaddr = 'your gmail username'
    password = 'your password'
    try:
        p = postman(host='smtp.gmail.com', auth=(fromaddr, password))
        print("\nLogin Successful!")
        break
    except:
        print("\nERROR: Credentials are incorrect. Please try again...")

def sendEmail_ok():
    fromaddr = 'your gmail username'
    password = 'your password'
    try:
        p = postman(host='smtp.gmail.com', auth=(fromaddr, password))
        r = p.send(email(
            content=u'<p>Your Appointment is Ready</p>',
            subject='Visa Booking',
            sender='System <system@system.com>',
            receivers=['receiver1@gmail.com', 'receiver2@gmail.com'],
            attachments=['booked.png']
        ))
        assert r.ok
        time.sleep(3)

    except:
        print("\nLogin unsuccessful, try again.")

def sendEmail_nok():
    fromaddr = 'your gmail username'
    password = 'your password'
    try:
        p = postman(host='smtp.gmail.com', auth=(fromaddr, password))
        r = p.send(email(
            content=u'<p>Your Appointment is Ready</p>',
            subject='Visa Booking',
            sender='System <system@system.com>',
            receivers=['receiver1@gmail.com', 'receiver2@gmail.com'],
            attachments=['unexpected_error.png']
        ))
        assert r.ok
        time.sleep(3)

    except:
        print("\nLogin unsuccessful, try again.")

def checkAvailability():
    print("\nChecking Availability...")
    #uk_site = "https://www.vfsvisaonline.com/Netherlands-Global-Online-Appointment_Zone2/AppScheduling/AppWelcome.aspx?P=b0KsiJlv+LIdjKDvIvW+nLNY7GnUFdfuwQj4DXbs4vo="
    site = "https://www.vfsvisaonline.com/Netherlands-Global-Online-Appointment_Zone2/AppScheduling/AppWelcome.aspx?P=%2FiOLWQz9Vk07YwT57Xup3WWpcMKp4QcG2ApaJBrIfls%3D"

    warnings.filterwarnings("ignore")
    chrome_options = Options()
    chrome_options.add_argument('--window-size=1920,1080')
    #chrome_options.headless = True

    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
    driver.get(site)

    try:
        appointment = driver.find_element_by_id("plhMain_lnkSchApp")
        appointment.click()
        Select(driver.find_element_by_id(
            "plhMain_cboVAC")).select_by_index(2)
        driver.find_element_by_id("plhMain_btnSubmit").click()

        person = driver.find_element_by_id("plhMain_tbxNumOfApplicants")
        person.send_keys(Keys.BACKSPACE)
        person.send_keys("2")

        Select(driver.find_element_by_id(
            "plhMain_cboVisaCategory")).select_by_index(6)
        driver.find_element_by_id("plhMain_btnSubmit").click()

        while("No date(s)" in driver.page_source):
            print(f"\nTrying Again")
            driver.refresh()

        time.sleep(2)
        Select(driver.find_element_by_id(
            "plhMain_repAppVisaDetails_cboTitle_0")).select_by_index(1)
        time.sleep(2)
        driver.find_element_by_name("ctl00$plhMain$repAppVisaDetails$ctl01$tbxFName").send_keys('FIRSTNAME1')
        time.sleep(2)
        driver.find_element_by_name("ctl00$plhMain$repAppVisaDetails$ctl01$tbxLName").send_keys('SURNAME1')
        time.sleep(2)
        driver.find_element_by_name("ctl00$plhMain$repAppVisaDetails$ctl01$tbxContactNumber").send_keys('PHONE NUMBER1')
        time.sleep(2)
        driver.find_element_by_name("ctl00$plhMain$repAppVisaDetails$ctl01$tbxEmailAddress").send_keys('username1@gmail.com')
        time.sleep(2)

        Select(driver.find_element_by_id("plhMain_repAppVisaDetails_cboTitle_1")).select_by_index(2)
        time.sleep(2)
        driver.find_element_by_name("ctl00$plhMain$repAppVisaDetails$ctl02$tbxFName").send_keys('FIRSTNAME2')
        time.sleep(2)
        driver.find_element_by_name("ctl00$plhMain$repAppVisaDetails$ctl02$tbxLName").send_keys('SURNAME2')
        time.sleep(2)
        driver.find_element_by_name("ctl00$plhMain$repAppVisaDetails$ctl02$tbxContactNumber").send_keys('PHONE NUMBER2')
        time.sleep(2)
        driver.find_element_by_name("ctl00$plhMain$repAppVisaDetails$ctl02$tbxEmailAddress").send_keys('username2@gmail.com')
        time.sleep(2)

        Select(driver.find_element_by_id("plhMain_cboConfirmation")).select_by_index(1)
        time.sleep(2)
        driver.find_element_by_id("plhMain_btnSubmit").click()
        time.sleep(30)

        while(True):
            driver.find_element_by_xpath(
                "//*[@id='plhMain_cldAppointment']/tbody/tr[1]/td/table/tbody/tr/td[3]/a").click()

            if ("Error in the application, please contact admin." in driver.page_source):
                print(f"\nReturns Error in June.")

            elif ("No date(s) available for current month." in driver.page_source):
                print(f"\nNo Appointments in June.")

            elif ("Appointments are" in driver.page_source):
                print("\nAvailable in June\n")
                time.sleep(5)
                driver.find_element_by_class_name("OpenDateAllocated").click()
                time.sleep(2)
                driver.find_element_by_id("plhMain_gvSlot_lnkTimeSlot_0").click()
                time.sleep(2)
                driver.switch_to.alert.accept()
                time.sleep(10)
                driver.save_screenshot('booked.png')
                time.sleep(10)
                sendEmail_ok()
                time.sleep(10)

            else:
                print("Unexpected Error")
                driver.save_screenshot('unexpected_error.png')
                time.sleep(10)
                sendEmail_nok()
                time.sleep(10)

            driver.find_element_by_xpath(
                "//*[@id='plhMain_cldAppointment']/tbody/tr[1]/td/table/tbody/tr/td[1]/a").click()

            if ("Error in the application, please contact admin." in driver.page_source):
                print(f"\nReturns Error in May.")

            elif ("No date(s) available for current month." in driver.page_source):
                print(f"\nNo Appointments in May.")

            elif ("Appointments are" in driver.page_source):
                print("\nAvailable in May\n")
                time.sleep(5)
                driver.find_element_by_class_name("OpenDateAllocated").click()
                time.sleep(2)
                driver.find_element_by_id("plhMain_gvSlot_lnkTimeSlot_0").click()
                time.sleep(2)
                driver.switch_to.alert.accept()
                time.sleep(10)
                driver.save_screenshot('booked.png')
                time.sleep(10)
                sendEmail_ok()
                time.sleep(10)

            else:
                print("Unexpected Error")
                driver.save_screenshot('unexpected_error.png')
                time.sleep(10)
                sendEmail_nok()
                time.sleep(10)

    finally:
        driver.quit()

checkAvailability()
