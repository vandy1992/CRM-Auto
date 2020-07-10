# import unittest
# import HtmlTestRunner
# import res as res
# from selenium import webdriver
# import requests
# import time
# from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from PageObjects.Login_Profile_Page import LoginPage
import pytest

class Sign_up_Page():
    #locators of all the element
    create = "//div[@class='preview-elements details-block mt-4']//div[contains(text(),'Create New Account')]"
    CreateNew = "/html[1]/body[1]/div[1]/div[1]/main[1]/div[2]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]"
    signup = "//b[contains(text(),'Sign Up')]"
    firstname = "//input[@name='first_name']"
    lastname = "//input[@name='last_name']"
    email = "//input[@name='primary_email']"
    password = "//input[@name='password']"
    repassword = "//input[@name='confirm_password']"
    countrydropdown = "//div[@class='dropdown']"
    phone_no = "//input[@name='phone_number']"
    male = "//span[contains(text(),'Male')]"
    female = "//span[contains(text(),'Female')]"
    others = "//span[contains(text(),'Custom')]"
    country = "//input[@placeholder='Select Country']"
    sign_up = "//button[@id='registerbtn']"

    Signup_Email = "2020digicollect5123@gmail.com"
    Signup_Password = "Digicollect_1233"

    def __init__(self,driver):
        self.driver=driver

    def Click_Signup(self):
        self.driver.find_element_by_xpath(self.signup).click()

    def FirstName(self,firstName):
        self.driver.find_element_by_xpath(self.firstname).send_keys(firstName)

    def LastName(self,lastName):
        self.driver.find_element_by_xpath(self.lastname).send_keys(lastName)

    def setemail(self,Signup_Email):
        self.driver.find_element_by_xpath(self.email).send_keys(Signup_Email)

    def setPassword(self,Signup_Password):
        self.driver.find_element_by_xpath(self.password).send_keys(Signup_Password)

    def Confirm_Password(self,Signup_Password):
        self.driver.find_element_by_xpath(self.repassword).send_keys(Signup_Password)

    def setPhoneno(self,PhoneNo):
        self.driver.find_element_by_xpath(self.phone_no).send_keys(PhoneNo)

    def clickFemale(self):
        self.driver.find_element_by_xpath(self.female).click()

    def clickMale(self):
        self.driver.find_element_by_xpath(self.male).click()

    def clickOthers(self):
        self.driver.find_element_by_xpath(self.others).click()

    def setcCountry(self,Country):
        dropdwn=self.driver.find_element_by_xpath(self.country)
        dropdwn.send_keys(Country)
        dropdwn.send_keys(Keys.ARROW_DOWN)
        dropdwn.send_keys(Keys.ENTER)

    def ClickSignup(self):
        self.driver.find_element_by_xpath(self.sign_up).click()




