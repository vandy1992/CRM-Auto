import unittest
import HtmlTestRunner
# import res as res
from selenium import webdriver
# import requests
import time
import sys
sys.path.append("C://Users/Vandana Mallaiah/PycharmProjects/CRM Automation")
# from PageObjects.Profile_Page import ProfilePage
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.keys import Keys
from PageObjects.Login_Profile_Page import LoginPage

class LoginTest(unittest.TestCase):
    # lOGIN PAGE
    email ="digicollect.com@gmail.com"
    password ="digicollect123"

    #email ="digicollect.com@gmail.com"
    # password ="digicollect123"

    editprofile="C:..\\Screenshoot\\Capture.JPG"
    lOGO="C:..\\Screenshoot\\tgr.jpg"

    # URL
    baseURL="https://testauth.digicollect.com/?redirect_to=https%3A%2F%2Ftestcrm.digicollect.com%2F"

    # ADDRESS
    firstName = "DigiCollect"
    middleName = ".com"
    lastName = "Intelligent Industrial Internet"
    Gender = "female"
    # DateOfBirth = "18/09/1992"
    BloodGroup = "B+"
    About = "one of the leading company"

    # COMMUNICATION
    P_P_NO="+919380501241"
    E_C_name="Naren"
    Relation="Colleague"
    E_C_no="+919980301317"
    M_ENote="Emergency At Office"
    Socialmedia="https://www.facebook.com/basu.chitti/"

    # ADDRESS
    Street = "4th Main Rd,"
    City = "Bangalore"
    Township = "Sampangi Rama Nagara,"
    State = "karnataka"
    Zip_Code = "560027"
    Country = "India"

    # PREFERENCES
    FavouriteFood = "biryani"
    FavouriteDrink = "coco-cola"
    Allergy = "maskmelon juise"
    roomtype="Double"
    bedtype="Medium"
    PillowType="Medium"
    bedsheetType="Cotton"

    driver = webdriver.Chrome(executable_path="..\\Drivers\\chromedriver.exe")

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()

    def test_loginpage(self):
        lp=LoginPage(self.driver)

        # lOGIN PAGE
        print("entering Login Page")
        lp.setUserEmail(self.email)
        lp.setPassword(self.password)
        self.driver.save_screenshot("C:..\\Screenshoot\\loginpage.png")
        lp.clickSignin()
        time.sleep(10)
        print("logged in and entered Profile")

        # PROFILE
        # lp.EDIT_PAGE(self.editprofile)
        # time.sleep(3)
        # lp.EDIT_Logo(self.lOGO)
        # time.sleep(3)
        lp.Click_profile()
        self.driver.save_screenshot("C:..\\Screenshoot\\Profilepage.png")
        time.sleep(5)
        # lp.ClickEdit()
        # time.sleep(5)

        # BASIC INFROMATION
        print("enterd Basic Information")
        lp.FirstName(self.firstName)
        time.sleep(5)
        lp.MiddleName(self.middleName)
        time.sleep(5)
        lp.LastName(self.lastName)
        lp.setfemale()
        time.sleep(5)
        # self.driver.execute_script("window.scrollBy(50,0)","")
        # lp.setdob()
        # time.sleep(5)
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

    #
    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.close()

if __name__=="__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='..\\Reports'))
