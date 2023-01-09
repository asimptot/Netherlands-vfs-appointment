from time import sleep
import yagmail
from selenium.webdriver.support.select import Select
from init import *

fromaddr = 'your gmail usernam'
app_password = 'your gmail token' #https://towardsdatascience.com/automate-sending-emails-with-gmail-in-python-449cc0c3c317
to = 'receiver1@gmail.com'

class Visa:
  def setup(self):
    Setup.init(self)
    sleep(4)

  def sendEmail_ok(self):
      subject = 'Visa Booking'
      content = ["Your Appointment is Ready", 'booked.png']
      try:
          with yagmail.SMTP(fromaddr, app_password) as yag:
              yag.send(to, subject, content)
              print('Sent email successfully')
          sleep(3)
      except:
          print("\nFailed to send email, try again.")

  def sendEmail_nok(self):
      subject = 'Error E-Mail'
      content = ["You can find an image file attached.", 'unexpected_error.png']
      try:
          with yagmail.SMTP(fromaddr, app_password) as yag:
              yag.send(to, subject, content)
              print('Sent email successfully')
          sleep(3)
      except:
          print("\nFailed to send email, try again.")

  def checkAvailability(self):
      print("\nChecking Availability...")
      site = "https://www.vfsvisaonline.com/Netherlands-Global-Online-Appointment_Zone2/AppScheduling/AppWelcome.aspx?P=%2FiOLWQz9Vk07YwT57Xup3WWpcMKp4QcG2ApaJBrIfls%3D"

      Visa.setup(self)
      self.driver.get(site)
      sleep(120)

      try:
          appointment = self.driver.find_element(By.ID, "plhMain_lnkSchApp")
          appointment.click()
          Select(self.driver.find_element(By.ID, "plhMain_cboVAC")).select_by_index(2)
          self.driver.find_element(By.ID, "plhMain_btnSubmit").click()

          person = self.driver.find_element(By.ID, "plhMain_tbxNumOfApplicants")
          person.send_keys(Keys.BACKSPACE)
          person.send_keys("2")

          Select(self.driver.find_element(By.ID, "plhMain_cboVisaCategory")).select_by_index(6)
          self.driver.find_element(By.ID, "plhMain_btnSubmit").click()

          while("No date(s)" in self.driver.page_source):
              print(f"\nTrying Again")
              self.driver.refresh()

          sleep(2)
          Select(self.driver.find_element(By.ID, "plhMain_repAppVisaDetails_cboTitle_0")).select_by_index(1)
          sleep(2)
          self.driver.find_element(By.NAME, "ctl00$plhMain$repAppVisaDetails$ctl01$tbxFName").send_keys('FIRSTNAME1')
          sleep(2)
          self.driver.find_element(By.NAME, "ctl00$plhMain$repAppVisaDetails$ctl01$tbxLName").send_keys('SURNAME1')
          sleep(2)
          self.driver.find_element(By.NAME, "ctl00$plhMain$repAppVisaDetails$ctl01$tbxContactNumber").send_keys('PHONE NUMBER1')
          sleep(2)
          self.driver.find_element(By.NAME, "ctl00$plhMain$repAppVisaDetails$ctl01$tbxEmailAddress").send_keys('username1@gmail.com')
          sleep(2)

          Select(self.driver.find_element(By.ID, "plhMain_repAppVisaDetails_cboTitle_1")).select_by_index(2)
          sleep(2)
          self.driver.find_element(By.NAME, "ctl00$plhMain$repAppVisaDetails$ctl02$tbxFName").send_keys('FIRSTNAME2')
          sleep(2)
          self.driver.find_element(By.NAME, "ctl00$plhMain$repAppVisaDetails$ctl02$tbxLName").send_keys('SURNAME2')
          sleep(2)
          self.driver.find_element(By.NAME, "ctl00$plhMain$repAppVisaDetails$ctl02$tbxContactNumber").send_keys('PHONE NUMBER2')
          sleep(2)
          self.driver.find_element(By.NAME, "ctl00$plhMain$repAppVisaDetails$ctl02$tbxEmailAddress").send_keys('username2@gmail.com')
          sleep(2)

          Select(self.driver.find_element(By.ID, "plhMain_cboConfirmation")).select_by_index(1)
          sleep(2)
          self.driver.find_element(By.ID, "plhMain_btnSubmit").click()
          sleep(30)

          while(True):
              self.driver.find_element(By.XPATH, "//*[@id='plhMain_cldAppointment']/tbody/tr[1]/td/table/tbody/tr/td[3]/a").click()

              if ("Error in the application, please contact admin." in self.driver.page_source):
                  print(f"\nReturns Error in June.")

              elif ("No date(s) available for current month." in self.driver.page_source):
                  print(f"\nNo Appointments in June.")

              elif ("Appointments are" in self.driver.page_source):
                  print("\nAvailable in June\n")
                  sleep(5)
                  self.driver.find_element(By.CLASS_NAME, "OpenDateAllocated").click()
                  sleep(2)
                  self.driver.find_element(By.ID, "plhMain_gvSlot_lnkTimeSlot_0").click()
                  sleep(2)
                  self.driver.switch_to.alert.accept()
                  sleep(10)
                  self.driver.save_screenshot('booked.png')
                  sleep(10)
                  Visa.sendEmail_ok(self)
                  sleep(10)

              else:
                  print("Unexpected Error")
                  self.driver.save_screenshot('unexpected_error.png')
                  sleep(10)
                  Visa.sendEmail_nok()
                  sleep(10)

              self.driver.find_element(By.XPATH, "//*[@id='plhMain_cldAppointment']/tbody/tr[1]/td/table/tbody/tr/td[1]/a").click()

              if ("Error in the application, please contact admin." in self.driver.page_source):
                  print(f"\nReturns Error in May.")

              elif ("No date(s) available for current month." in self.driver.page_source):
                  print(f"\nNo Appointments in May.")

              elif ("Appointments are" in self.driver.page_source):
                  print("\nAvailable in May\n")
                  sleep(5)
                  self.driver.find_element(By.CLASS_NAME, "OpenDateAllocated").click()
                  sleep(2)
                  self.driver.find_element(By.ID, "plhMain_gvSlot_lnkTimeSlot_0").click()
                  sleep(2)
                  self.driver.switch_to.alert.accept()
                  sleep(10)
                  self.driver.save_screenshot('booked.png')
                  sleep(10)
                  Visa.sendEmail_ok(self)
                  sleep(10)

              else:
                  print("Unexpected Error")
                  self.driver.save_screenshot('unexpected_error.png')
                  sleep(10)
                  Visa.sendEmail_nok(self)
                  sleep(10)

      finally:
          self.driver.quit()

v = Visa()
v.checkAvailability()
