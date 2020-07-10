import unittest
import HtmlTestRunner
import pytest
# import res as res
from selenium import webdriver
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import allure
from allure_commons.types import AttachmentType
import time
from selenium.webdriver.support.wait import WebDriverWait
from PageObjects.Login_Profile_Page import LoginPage
import sys
sys.path.append("C://Users/Vandana Mallaiah/PycharmProjects/CRM")
from PageObjects.Signup_Page import Sign_up_Page
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.keys import Keys
# driver = webdriver.Chrome(executable_path="..\\Drivers\\chromedriver.exe")

#https://quirky-bose-44bd7b.netlify.app/

class SignUPTest(unittest.TestCase):
    baseURL = "https://testauth.digicollect.com/?redirect_to=https%3A%2F%2Ftestcrm.digicollect.com%2F"
    firstName="Digi"
    lastName ="Collect"
    registered_email = " savifm11105288@gmail.com"
    registered_password ="Digicollect_1233"
    # confirm_Password ="digicollect123"
    Country="India"
    PhoneNo="+919380501241"
    driver = webdriver.Chrome(executable_path="..\\Drivers\\chromedriver.exe")
    # driver = webdriver.Chrome(executable_path="E:\chromedriver_win32\chromedriver.exe")

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()
    @allure.severity(allure.severity_level.BLOCKER)
    def test_SignUp(self):
        sp=Sign_up_Page(self.driver)
        print("Sign Up Page")
        self.driver.save_screenshot("C:..\\Screenshots\\Signup_page.png")
        sp.Click_Signup()
        time.sleep(5)
        allure.attach(self.driver.get_screenshot_as_png(), name="signuppage", attachment_type=AttachmentType.PNG)
        sp.FirstName(self.firstName)
        sp.LastName(self.lastName)
        sp.setemail(self.registered_email)
        time.sleep(3)
        sp.setPassword(self.registered_password)
        time.sleep(3)
        sp.Confirm_Password(self.registered_password)
        time.sleep(3)
        sp.setPhoneno(self.PhoneNo)
        time.sleep(3)
        sp.clickFemale()
        time.sleep(3)
        sp.setcCountry(self.Country)
        time.sleep(3)
        sp.ClickSignup()
        time.sleep(5)
        token = requests.post(url="https://testauth.digicollect.com/auth",
                              json={"email": self.registered_email, "password": self.registered_password}).json()
        if not token.get("access_token"):
            token = requests.post(url="https://testauth.digicollect.com/auth",
                                  json={"email": self.registered_email, "password": self.registered_password}).json()
        print(token)
        self.driver.save_screenshot("C:..\\Screenshots\\OTP_Page.png")
        access_token = token.get("access_token")
        if access_token:
            otp = requests.get("https://testcrmapis.digicollect.com/users/get_otp",
                               headers={"Authorization": access_token}).json()
            if otp.get('status_id') == 0:
                otp = requests.get("https://testcrmapis.digicollect.com/users/get_otp",
                                   headers={"Authorization": access_token}).json()
            print(otp)
            res = list(otp.keys())[0]
            print(otp[res])
            print("otp generated")

            def otp_number(self):
                time.sleep(2)
                wait = WebDriverWait(self.driver, 100).until(
                    EC.presence_of_element_located((By.XPATH, "(//input[@type='number'])[1]")))
                element = self.driver.find_element_by_xpath("(//input[@type='number'])[1]")
                element.click()
                element.send_keys(otp[res])
                time.sleep(10)
            otp_number(self)
            allure.attach(self.driver.get_screenshot_as_png(), name="OTP_page", attachment_type=AttachmentType.PNG)

        # ADDRESS

    FirstName = "DigiCollect"
    MiddleName = ".com"
    LastName = "Intelligent Industrial Internet"
    Gender = "female"
    # DateOfBirth = "18/09/1992"
    BloodGroup = "A+"
    About = "one of the leading company"

    # COMMUNICATION
    P_P_NO = "+919380501241"
    E_C_name = "Naren"
    Relation = "Colleague"
    E_C_no = "+919980301317"
    M_ENote = "Emergency At Office"
    Socialmedia = "https://www.facebook.com/basu.chitti/"


    # ADDRESS
    Street = "4th Main Rd,"
    City = "Bangalore"
    Township = "Sampangi Rama Nagara,"
    State = "karnataka"
    Zip_Code = "560027"
    country = "India"

    # PREFERENCES
    FavouriteFood = "biryani"
    FavouriteDrink = "coco-cola"
    Allergy = "maskmelon juise"
    roomtype = "Double"
    bedtype = "Medium"
    PillowType = "Medium"
    bedsheetType = "Cotton"

    @allure.severity(allure.severity_level.MINOR)
    def test_loginpage(self):
        lp=LoginPage(self.driver)
        allure.attach(self.driver.get_screenshot_as_png(), name="loginpage", attachment_type=AttachmentType.PNG)
        time.sleep(5)
        lp.Click_profile()
        allure.attach(self.driver.get_screenshot_as_png(), name="HOME_page", attachment_type=AttachmentType.PNG)
        # self.driver.save_screenshot("C:..\\Screenshoot\\Profilepage.png")
        time.sleep(5)
        lp.ClickEdit()
        time.sleep(5)

        # BASIC INFROMATION
        print("enterd Basic Information")
        lp.FirstName(self.FirstName)
        time.sleep(5)
        lp.MiddleName(self.MiddleName)
        time.sleep(5)
        lp.LastName(self.LastName)
        lp.setfemale()
        time.sleep(5)
        # self.driver.execute_script("window.scrollBy(50,0)","")
        lp.setdob()
        time.sleep(5)
        lp.setbloodgroup()
        time.sleep(5)
        lp.setabout(self.About)
        lp.setSave()
        time.sleep(3)
        lp.accept()
        time.sleep(5)
        print("Enterd Communication")

        # COMMUNICATION
        lp.Click_communication()
        time.sleep(3)
        allure.attach(self.driver.get_screenshot_as_png(), name="commuication", attachment_type=AttachmentType.PNG)
        lp.Click_Edit()
        time.sleep(5)
        #     # lp.Click_puls()
        lp.setP_P_no(self.P_P_NO)
        time.sleep(3)
        lp.set_E_C_Name(self.E_C_name)
        time.sleep(3)
        lp.setRelation(self.Relation)
        time.sleep(3)
        lp.setE_C_no(self.E_C_no)
        time.sleep(3)
        lp.setM_E_Note(self.M_ENote)
        time.sleep(3)
        lp.setSocial_media(self.Socialmedia)
        lp.setSave()
        time.sleep(3)
        lp.accept()
        time.sleep(3)
        #
        # ADDRESS
        print("enterd Address")
        lp.Click_Address()
        time.sleep(3)
        allure.attach(self.driver.get_screenshot_as_png(), name="address", attachment_type=AttachmentType.PNG)
        lp.Click_Edit()
        time.sleep(3)
        lp.setStreet(self.Street)
        time.sleep(3)
        lp.setTown(self.Township)
        time.sleep(3)
        lp.setZipcode(self.Zip_Code)
        time.sleep(3)
        lp.setCity(self.City)
        time.sleep(3)
        lp.setState(self.State)
        time.sleep(3)
        lp.setSave()
        time.sleep(3)
        lp.accept()
        time.sleep(3)
        #
        # PREFERENCES
        print("enterd Preferences")
        lp.Click_Preferences()
        time.sleep(3)
        allure.attach(self.driver.get_screenshot_as_png(), name="Preferences", attachment_type=AttachmentType.PNG)
        lp.Click_Edit()
        time.sleep(5)
        lp.setFood(self.FavouriteFood)
        lp.setDrink(self.FavouriteDrink)
        lp.setAllergy(self.Allergy)
        lp.Click_medium_spice()
        lp.Click_non_veg()
        lp.Click_organic()
        lp.Click_Low_colestol()
        lp.setRoomtype(self.roomtype)
        time.sleep(3)
        lp.setPillowType(self.PillowType)
        time.sleep(3)
        lp.setBedtype(self.bedtype)
        time.sleep(3)
        lp.setBedsheetType(self.bedsheetType)
        time.sleep(3)
        print("Ended with Profile")
        lp.setSave()
        time.sleep(3)
        # self.driver.close()

    # @classmethod
    # def tearDownClass(cls):
    #    cls.driver.close()

if __name__=="__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='..\\Reports'))






