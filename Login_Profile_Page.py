import time
from selenium.webdriver.common.keys import Keys
class LoginPage():
    #Locators of all the web element
    email_id="emailaddress"
    password_name="password"
    signin_xpath="//button[@class='btn btn-block btn-gradient fuse-ripple-ready']"
    forgot_password_xpath="//small[contains(text(),'Forgot your password?')]"
    signUp_xpth="//b[contains(text(),'Sign Up')]"
    # Edit = "/html[1]/body[1]/div[1]/div[1]/main[1]/div[2]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/a[1]"
    # profile="//span[contains(text(),'Profile')]"

    Edit_Profile="//*[@id='5ee862d248f10c2a008633f2']/div[1]/div[2]/div/div[1]/div/div[1]/div[1]/div/label/span"
    logo="//label[@class='profilePicEdit']"

    Basic_information = "//a[@class='nav-link mb-2 active']"
    Edit = "//a[contains(text(),'Edit')]"
    profile = "//span[contains(text(),'Profile')]"
    firstname = "//input[@name='first_name']"
    middlename = "//input[@name='middle_name']"
    lastname = "//input[@name='last_name']"
    female = "//span[contains(text(),'Female')]"
    male="//span[contains(text(),'Male')]"
    custom="//span[contains(text(),'Custom')]"
    dob = "//input[@name='date']"
    bloodgroup = "//div[@name='bloodgroup']"
    # A-="//span[@class='selected-tag'][1]"

    about = "//textarea[@name='about']"
    # Save="/html[1]/body[1]/div[1]/div[1]/main[1]/div[2]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/button[2]"
    one ="//tr[1]//td[2]"
    ten="//td[@class='cell cur-month'][contains(text(),'10')]"
    year="//a[@class='mx-current-year'][contains(text(),'2020')]"
    arrow="//a[@class='mx-icon-last-year']"
    Year1="//span[contains(text(),'2016')]"
    march="//span[@class='cell'][contains(text(),'Mar')]"
    apply="//button[@class='mx-datepicker-btn mx-datepicker-btn-confirm']"
    # ok="/html[1]/body[1]/div[2]/div[1]/div[3]/button[1]"
    ok="//button[@class='swal2-confirm swal2-styled']"
    group="/html[1]/body[1]/div[1]/div[1]/main[1]/div[2]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[6]/div[1]/div[2]/span[1]/div[1]/div[1]/div[1]/span[1]"


    #constructor

    def __init__(self,driver):
        self.driver=driver

    # LOGIN PAGE
    def setUserEmail(self,email):
        self.driver.find_element_by_id(self.email_id).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element_by_name(self.password_name).send_keys(password)

    def clickSignin(self):
        self.driver.find_element_by_xpath(self.signin_xpath).click()

    # PROFILE
    # BASIC INFORMATION
    def ClickEdit(self):
        self.driver.find_element_by_xpath(self.Edit).click()

    def EDIT_PAGE(self,editprofile):
        # self.driver.find_element_by_xpath(self.firstname).clear()
        self.driver.find_element_by_xpath(self.Edit_Profile).click()
        self.driver.find_element_by_xpath(self.Edit_Profile).send_keys(editprofile)

    def EDIT_Logo(self,logo):
        # self.driver.find_element_by_xpath(self.firstname).clear()
        self.driver.find_element_by_xpath(self.Edit_Profile).click()
        self.driver.find_element_by_xpath(self.Edit_Profile).send_keys(logo)

    def Click_profile(self):
        self.driver.find_element_by_xpath(self.profile).click()

    def setcancel(self, Cancel):
        self.driver.find_element_by_xpath(self.about).click()

    def setsave(self):
        self.driver.find_element_by_xpath(self.Save).click()

    def accept(self):
        self.driver.find_element_by_xpath(self.ok).click()

    def Clickprofile(self):
        self.driver.find_element_by_xpath(self.profile).click()

    def Click_Edit(self):
        self.driver.find_element_by_xpath(self.Edit).click()

    def FirstName(self,firstName):
        self.driver.find_element_by_xpath(self.firstname).clear()
        time.sleep(3)
        self.driver.find_element_by_xpath(self.firstname).send_keys(firstName)

    def MiddleName(self,middleName):
        self.driver.find_element_by_xpath(self.middlename).clear()
        self.driver.find_element_by_xpath(self.middlename).send_keys(middleName)

    def LastName(self,lastName):
        self.driver.find_element_by_xpath(self.lastname).clear()
        self.driver.find_element_by_xpath(self.lastname).send_keys(lastName)

    def setfemale(self):
        # self.driver.find_element_by_xpath(self.gender).clear()
        self.driver.find_element_by_xpath(self.female).click()

    def setmale(self):
        # self.driver.find_element_by_xpath(self.gender).clear()
        self.driver.find_element_by_xpath(self.male).click()

    def setcustom(self):
        # self.driver.find_element_by_xpath(self.gender).clear()
        self.driver.find_element_by_xpath(self.custom).click()

    def setdob(self):
        # self.driver.find_element_by_xpath(self.dob).clear()
        self.driver.find_element_by_xpath(self.dob).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(self.year).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(self.arrow).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(self.Year1).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(self.march).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(self.ten).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(self.apply).click()
        time.sleep(5)

    def setbloodgroup(self):
        # self.driver.find_element_by_xpath(self.bloodgroup).clear()
        self.driver.find_element_by_xpath(self.bloodgroup).click()
        time.sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[1]/div/main/div[2]/div/section/div/div[1]/div/div/div[1]/div[2]/div/div[2]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[6]/div/div[2]/span/div/ul/li[3]/a").click()
        time.sleep(3)


    def setabout(self,About):

        self.driver.find_element_by_xpath(self.about).clear()
        time.sleep(3)
        self.driver.find_element_by_xpath(self.about).send_keys(About)

    # Locators of COMMUNICATION

    communication = "//h6[contains(text(),'Communication')]"
    plus="//*[@id='communicationtab']/div/div/div/div/div[2]/div/div/div[1]/div/div[2]/span/span"
    Personal_Email = "//input[@name='primary_email0']"
    Alternate_email="// input[ @ name = 'primary_email0']"
    Personal_Phone_Number = "//input[@name='phone_number']"
    Emergency_Contact_Name = "//input[@name='emergency_contact_name']"
    Relationship = "//input[@name='emergency_contact_relationship']"
    Emergency_Contact_Number = "//input[@name='emergency_contact_number']"
    Medical_Emergency_Notes = "//textarea[@name='emergency_notes']"
    Social_Media = "//input[@name='media_url0']"
    dropdown="//div[@class='dropdown-toggle pointer bottomBorder socialMedia']"
    Save="/html[1]/body[1]/div[1]/div[1]/main[1]/div[2]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/button[2]"

    def Click_communication(self):
        self.driver.find_element_by_xpath(self.communication).click()

    def Click_puls(self):
        self.driver.find_element_by_xpath(self.plus).click()

    def setP_Email(self, P_email):
        self.driver.find_element_by_xpath(self.Personal_Email).send_keys(P_email)

    def setP_P_no(self, P_P_NO):
        self.driver.find_element_by_xpath(self.Personal_Phone_Number).clear()
        time.sleep(2)
        self.driver.find_element_by_xpath(self.Personal_Phone_Number).send_keys(P_P_NO)

    def set_E_C_Name(self, E_C_name):
        self.driver.find_element_by_xpath(self.Emergency_Contact_Name).clear()
        time.sleep(2)
        self.driver.find_element_by_xpath(self.Emergency_Contact_Name).send_keys(E_C_name)

    def setRelation(self, Relation):
        self.driver.find_element_by_xpath(self.Relationship).clear()
        time.sleep(2)
        self.driver.find_element_by_xpath(self.Relationship).send_keys(Relation)

    def setE_C_no(self, E_C_no):
        self.driver.find_element_by_xpath(self.Emergency_Contact_Number).clear()
        time.sleep(2)
        self.driver.find_element_by_xpath(self.Emergency_Contact_Number).send_keys(E_C_no)

    def setM_E_Note(self, M_ENote):
        self.driver.find_element_by_xpath(self.Medical_Emergency_Notes).clear()
        time.sleep(2)
        self.driver.find_element_by_xpath(self.Medical_Emergency_Notes).send_keys(M_ENote)

    def setSocial_media(self, Socialmedia):
        self.driver.find_element_by_xpath(self.Social_Media).clear()
        time.sleep(2)
        self.driver.find_element_by_xpath(self.Social_Media).send_keys(Socialmedia)

    def setSave(self):
        self.driver.find_element_by_xpath(self.Save).click()


    # Locators of ADDRESS
    address = "//div[@class='digicontainer']//li[3]//a[1]"
    Street = "//input[@name='street']"
    City = "//input[@name='city']"
    Township = "//input[@name='township']"
    State = "//input[@name='state']"
    Zip_Code = "//input[@name='pin_code']"
    Country = "//span[@class='selected-tag']"

    def Click_Address(self):
        self.driver.find_element_by_xpath(self.address).click()

    def setStreet(self, street):
        self.driver.find_element_by_xpath(self.Street).clear()
        time.sleep(2)
        self.driver.find_element_by_xpath(self.Street).send_keys(street)

    def setCity(self, city):
        self.driver.find_element_by_xpath(self.City).clear()
        time.sleep(2)
        self.driver.find_element_by_xpath(self.City).send_keys(city)

    def setTown(self, Town):
        self.driver.find_element_by_xpath(self.Township).clear()
        time.sleep(2)
        self.driver.find_element_by_xpath(self.Township).send_keys(Town)

    def setState(self, state):
        self.driver.find_element_by_xpath(self.State).clear()
        time.sleep(2)
        self.driver.find_element_by_xpath(self.State).send_keys(state)

    def setZipcode(self, zipcode):
        self.driver.find_element_by_xpath(self.Zip_Code).clear()
        time.sleep(2)
        self.driver.find_element_by_xpath(self.Zip_Code).send_keys(zipcode)

    def setCountry(self, Country):
        dropdwn = self.driver.find_element_by_xpath(self.Country)
        dropdwn.send_keys(Country)
        dropdwn.send_keys(Keys.ARROW_DOWN)
        dropdwn.send_keys(Keys.ENTER)

    # PREFERENCES
    preferences ="//h6[contains(text(),'Preferences')]"
    Favourite_Food = "//input[@name='favourite_food']"
    Favourite_Drink = "//input[@name='favourite_drink']"
    Food_Allergy = "//input[@name='food_allergy']"
    # Dietary_Preferences = "//div[@class='digicontainer']//div[4]//div[1]//div[2]"
    medium_spice="//span[contains(text(),'Medium Spicy')]"
    organic="//span[contains(text(),'Organic')]"
    Low_colestrol="//span[contains(text(),'Low Cholesterol')]"
    non_veg="//span[contains(text(),'Non-Vegetarian')]"
    Room_Type = "//input[@placeholder='Select Room Type']"
    Pillow_Type = "//input[@placeholder='Select Pillow Type']"
    Bed_TypE = "//input[@placeholder='Select Bed Type']"
    Bedsheet_Type = "//input[@placeholder='Select Bed Sheet Type']"

    def Click_Preferences(self):
        self.driver.find_element_by_xpath(self.preferences).click()

    def setFood(self, FavouriteFood):
        self.driver.find_element_by_xpath(self.Favourite_Food).send_keys(FavouriteFood)

    def setDrink(self, FavouriteDrink):
        self.driver.find_element_by_xpath(self.Favourite_Drink).send_keys(FavouriteDrink)

    def setAllergy(self, Allergy):
        self.driver.find_element_by_xpath(self.Food_Allergy).send_keys(Allergy)

    def Click_medium_spice(self):
        self.driver.find_element_by_xpath(self.medium_spice).click()

    def Click_organic(self):
        self.driver.find_element_by_xpath(self.organic).click()

    def Click_Low_colestol(self):
        self.driver.find_element_by_xpath(self.Low_colestrol).click()

    def Click_non_veg(self):
        self.driver.find_element_by_xpath(self.non_veg).click()

    # def setDiet(self, Diet):
    #     self.driver.find_element_by_xpath(self.Dietary_Preferences).send_keys(Diet)

    def setRoomtype(self, roomtype):
        Room= self.driver.find_element_by_xpath(self.Room_Type)
        Room.send_keys(roomtype)
        # Room.send_keys(Keys.ARROW_DOWN)
        Room.send_keys(Keys.ENTER)

    def setBedtype(self, bedtype):
        # self.driver.find_element_by_xpath(self.Bed_TypE).send_keys()
        bed = self.driver.find_element_by_xpath(self.Bed_TypE)
        bed.send_keys(bedtype)
        # bed.send_keys(Keys.ARROW_DOWN)
        bed.send_keys(Keys.ENTER)

    def setPillowType(self, PillowType):
        pillow=self.driver.find_element_by_xpath(self.Pillow_Type)
        pillow.send_keys(PillowType)
        pillow.send_keys(Keys.ENTER)

    def setBedsheetType(self, bedsheetType):
        bedsheet=self.driver.find_element_by_xpath(self.Bedsheet_Type)
        bedsheet.send_keys(bedsheetType)
        bedsheet.send_keys(Keys.ENTER)
