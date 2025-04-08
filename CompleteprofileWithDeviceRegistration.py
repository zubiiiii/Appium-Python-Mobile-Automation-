import self
from appium import webdriver
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.action_chains import ActionChains


# Function to start the Appium driver
def start_driver():
    desired_caps = {
        'platformName': 'Android',  # or 'iOS'
        'automationName': "uiautomator2",
        'deviceName': "auto api 34",
        'app': 'C:/Users/TLS/Desktop/New folder/New folder/TLH_uat_20250328_1.0.apk',  # path to your app
        'appPackage': "sa.thelendinghub",
        "appactivity": "sa.thelendinghub.view.MainActivity",
        "autoGrantPermissions": True
    }

    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
    return driver


class ActionVariables:
    def __init__(self):
        # Define all variables in the constructor
        self.id_number = '1081383188'  # ID Number variable
        self.cell_number='544639515'
        self.email='zubais5dr@mailinator.com'
    def get_id_number(self):
        return self.id_number

    def get_cell_number(self):
        return self.cell_number

    def get_email(self):
        return self.email


# Function to perform actions (e.g., click two buttons)
def perform_action(driver):
    try:

        action_vars = ActionVariables()
        driver.implicitly_wait(7)

        # time.sleep(5)
        # AllowNotification = driver.find_elements(By.XPATH, 'com.android.permissioncontroller:id/permission_allow_button')  # Button 1 ID
        # AllowNotification.click()  # Click the first button
        # print("Allow notification > Allow")

        # Finding and clicking the first button
        # time.sleep(10)
        # Permissionallow=driver.find_element(By.ID,"com.android.permissioncontroller:id/permission_allow_button")
        # Permissionallow.click()
        time.sleep(9)

        Languagestartenlish = driver.find_element(By.ID, 'sa.thelendinghub:id/btnEnglish')  # Button 1 ID
        Languagestartenlish.click()  # Click the first button
        print("Language start english")

        # driver.implicitly_wait(7)
        # Finding and clicking the second button
        onboarding1 = driver.find_element(By.XPATH,
                                          "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.RelativeLayout")  # Button 2 ID
        onboarding1.click()  # Click the second button
        print("Premium fintech platform of Saudia Arabic")

        driver.implicitly_wait(7)
        onboarding2 = driver.find_element(By.XPATH,
                                          "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.RelativeLayout")  # Button 2 ID
        onboarding2.click()  # Click the second button
        print("Investmet at its simplest")

        driver.implicitly_wait(7)
        onboarding3 = driver.find_element(By.XPATH,
                                          "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.RelativeLayout")  # Button 2 ID
        onboarding3.click()  # Click the second button
        print("Apply for financing is a breeze")

        driver.implicitly_wait(7)
        onboarding4 = driver.find_element(By.XPATH,
                                          "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.RelativeLayout")  # Button 2 ID
        onboarding4.click()  # Click the second button
        print("Button 2 Clicked")

        driver.implicitly_wait(7)

        loginbluescreen = driver.find_element(By.ID, "sa.thelendinghub:id/btnLogin")
        loginbluescreen.click()  # Click the second button
        print("login button validation")

        driver.implicitly_wait(7)
        enterID = driver.find_element(By.ID, "sa.thelendinghub:id/editIdNumber")
        enterID.send_keys(action_vars.get_id_number())  # Click the second button
        print("inserting id")

        loginbluescreen = driver.find_element(By.ID, "sa.thelendinghub:id/btnLogin")
        loginbluescreen.click()  # Click the second button
        print("submit button ")
        driver.implicitly_wait(7)

        # Registernowbutton = driver.find_element(By.ID,"sa.thelendinghub: id / imgBtnRegister")
        # Registernowbutton.click()  # Click the second button
        # print("re ")
        # driver.implicitly_wait(7)

        time.sleep(7)
        Deviceregistration = driver.find_element(By.XPATH,
                                                 '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.RelativeLayout')
        Deviceregistration.click()
        print("Device registration ")
        driver.implicitly_wait(7)

        # time.sleep(5)
        driver.implicitly_wait(40)
        addphone = driver.find_element(By.ID, "sa.thelendinghub:id/editCellNumber")
        addphone.send_keys(action_vars.get_cell_number())
        print("cell number ")

        # driver.implicitly_wait(7)
        # selectdob=driver.find_element(By.ID,'sa.thelendinghub:id/editDob')
        # selectdob.send_keys("october 28, 1990")
        # print("select month ")
        # time.sleep(20)

        # actions = ActionChains(driver)
        driver.implicitly_wait(40)
        ViewCalendar = driver.find_element(By.ID, "sa.thelendinghub:id/imageViewCalendar")
        ViewCalendar.click()
        print("click view calendar ")
        #
        driver.implicitly_wait(40)
        # # time.sleep(15)
        # SelectYear=driver.find_element(By.ID,'android:id/date_picker_header_year')
        # SelectYear.click()
        # print("Select Year ")
        # driver.implicitly_wait(40)
        #
        # SelectYear = driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.DatePicker/android.widget.LinearLayout/android.widget.ScrollView/android.widget.ViewAnimator/android.widget.ListView/android.widget.TextView[2]')
        # SelectYear.click()
        # print("Select Year click ")
        # driver.implicitly_wait(40)
        #
        # Dobokbutton = driver.find_element(By.ID, 'android:id/button1')
        # Dobokbutton.click()
        # print("DOB ok button ")
        # driver.implicitly_wait(40)

        #
        # driver.implicitly_wait(40)
        # Okbutton=driver.find_element(By.ID,'android:id/button1')
        # Okbutton.click()
        # print("Ok")

        time.sleep(20)
        Proceed = driver.find_element(By.XPATH,
                                      "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout[4]/android.widget.RelativeLayout/android.widget.TextView")
        Proceed.click()
        print("Proceed to Verification button ")
        driver.implicitly_wait(40)

        RegistrationOTP1 = driver.find_element(By.ID, "sa.thelendinghub:id/pin_digit_1")
        RegistrationOTP1.send_keys("0")
        print("OTP digit 1 ")

        RegistrationOTP2 = driver.find_element(By.ID, "sa.thelendinghub:id/pin_digit_2")
        RegistrationOTP2.send_keys("0")
        print("OTP digit 2 ")

        RegistrationOTP3 = driver.find_element(By.ID, "sa.thelendinghub:id/pin_digit_3")
        RegistrationOTP3.send_keys("0")
        print("OTP digit 3 ")

        RegistrationOTP4 = driver.find_element(By.ID, "sa.thelendinghub:id/pin_digit_4")
        RegistrationOTP4.send_keys("0")
        print("OTP digit 4 ")

        RegistrationOTP5 = driver.find_element(By.ID, "sa.thelendinghub:id/pin_digit_5")
        RegistrationOTP5.send_keys("0")
        print("OTP digit 5 ")

        RegistrationOTP6 = driver.find_element(By.ID, "sa.thelendinghub:id/pin_digit_6")
        RegistrationOTP6.send_keys("00")
        print("OTP digit 6 ")
        #
        driver.implicitly_wait(40)
        OTPVerifyCredentials = driver.find_element(By.XPATH,
                                                   "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.RelativeLayout")
        OTPVerifyCredentials.click()
        print("OTPVerifyCredentials ")

        driver.implicitly_wait(40)

        LoginPIN1 = driver.find_element(By.ID, "sa.thelendinghub:id/pin_digit_1")
        LoginPIN1.send_keys("9")
        print("login Pin Code 1 ")

        driver.implicitly_wait(40)

        LoginPIN2 = driver.find_element(By.ID, "sa.thelendinghub:id/pin_digit_2")
        LoginPIN2.send_keys("8")
        print("login Pin Code 2 ")

        LoginPIN3 = driver.find_element(By.ID, "sa.thelendinghub:id/pin_digit_3")
        LoginPIN3.send_keys("7")
        print("login Pin Code 3 ")

        LoginPIN4 = driver.find_element(By.ID, "sa.thelendinghub:id/pin_digit_4")
        LoginPIN4.send_keys("6")
        print("login Pin Code 4 ")

        LoginPIN5 = driver.find_element(By.ID, "sa.thelendinghub:id/pin_digit_5")
        LoginPIN5.send_keys("5")
        print("login Pin Code 5 ")

        LoginPIN6 = driver.find_element(By.ID, "sa.thelendinghub:id/pin_digit_6")
        LoginPIN6.send_keys("4")
        print("login Pin Code 6 ")

        continiuelogin = driver.find_element(By.XPATH,
                                             "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout[4]/android.widget.RelativeLayout")
        continiuelogin.click()
        print("continiue login ")

        LoginOTP1 = driver.find_element(By.ID, "sa.thelendinghub:id/pin_digit_1")
        LoginOTP1.send_keys("0")
        print("login OTP 1 ")

        driver.implicitly_wait(40)

        LoginOTP2 = driver.find_element(By.ID, "sa.thelendinghub:id/pin_digit_2")
        LoginOTP2.send_keys("0")
        print("login OTP 2 ")

        LoginOTP3 = driver.find_element(By.ID, "sa.thelendinghub:id/pin_digit_3")
        LoginOTP3.send_keys("0")
        print("Login OTP 3 ")

        LoginOTP4 = driver.find_element(By.ID, "sa.thelendinghub:id/pin_digit_4")
        LoginOTP4.send_keys("0")
        print("Login OTP 4 ")

        LoginOTP5 = driver.find_element(By.ID, "sa.thelendinghub:id/pin_digit_5")
        LoginOTP5.send_keys("0")
        print("Login OTP 5 ")

        LoginOTP6 = driver.find_element(By.ID, "sa.thelendinghub:id/pin_digit_6")
        LoginOTP6.send_keys("0")
        print("Login OTP 6 ")

        LoginOTPverifycredentials = driver.find_element(By.XPATH,
                                                        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.RelativeLayout")
        LoginOTPverifycredentials.click()
        driver.implicitly_wait(10)

        Completeprofiletile = driver.find_element(By.ID, "sa.thelendinghub:id/cardviewCompleteProfile")
        Completeprofiletile.click()
        print("click Complete profile tile")
        driver.implicitly_wait(40)

        PersnoldetailNextbutton = driver.find_element(By.XPATH,
                                                      "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout[1]/android.widget.RelativeLayout")
        PersnoldetailNextbutton.click()
        print("Persnal detail Next button")
        driver.implicitly_wait(40)

        # occupation and Employer
        Sector = driver.find_element(By.XPATH,
                                     "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout[1]/androidx.cardview.widget.CardView/android.widget.LinearLayout/android.widget.Spinner")
        Sector.click()
        print("click sector")
        driver.implicitly_wait(40)

        Sectorvalue = driver.find_element(By.XPATH,
                                          "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.view.ViewGroup[2]/android.widget.TextView")
        Sectorvalue.click()
        print("Sector Value")
        driver.implicitly_wait(40)

        Jobtitle = driver.find_element(By.XPATH,
                                       "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout[2]/androidx.cardview.widget.CardView/android.widget.LinearLayout/android.widget.Spinner")
        Jobtitle.click()
        print("click job title")
        driver.implicitly_wait(40)

        Jobtitlevalue = driver.find_element(By.XPATH,
                                            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.view.ViewGroup[2]/android.widget.TextView")
        Jobtitlevalue.click()
        print("Jobtitlevalue")
        driver.implicitly_wait(40)

        Natureoffield = driver.find_element(By.XPATH,
                                            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout[3]/androidx.cardview.widget.CardView/android.widget.LinearLayout/android.widget.Spinner")
        Natureoffield.click()
        print("nature of field click")
        driver.implicitly_wait(40)

        Natureoffieldvalue = driver.find_element(By.XPATH,
                                                 "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.view.ViewGroup[2]/android.widget.TextView")
        Natureoffieldvalue.click()
        print("nature of field value")
        driver.implicitly_wait(40)

        Education = driver.find_element(By.XPATH,
                                        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout[4]/androidx.cardview.widget.CardView/android.widget.LinearLayout/android.widget.Spinner")
        Education.click()
        print("Education click")
        driver.implicitly_wait(40)

        Educationvalue = driver.find_element(By.XPATH,
                                             "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.view.ViewGroup[2]/android.widget.TextView")
        Educationvalue.click()
        print("Education value")
        driver.implicitly_wait(40)

        occupationandEmployerNextbutton = driver.find_element(By.XPATH,
                                                              "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout[6]/android.widget.RelativeLayout")
        occupationandEmployerNextbutton.click()
        print("occupation and Employer Next button")
        driver.implicitly_wait(40)

        # Family details
        Homeownership = driver.find_element(By.XPATH,
                                            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout[1]/androidx.cardview.widget.CardView/android.widget.LinearLayout/android.widget.Spinner")
        Homeownership.click()
        print("Homeownership")
        driver.implicitly_wait(40)

        Homeownershipvalue = driver.find_element(By.XPATH,
                                                 "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.view.ViewGroup[2]/android.widget.TextView")
        Homeownershipvalue.click()
        print("Homeownership value")
        driver.implicitly_wait(40)

        TypeofHome = driver.find_element(By.XPATH,
                                         "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout[2]/androidx.cardview.widget.CardView/android.widget.LinearLayout/android.widget.Spinner")
        TypeofHome.click()
        print("TypeofHome")
        driver.implicitly_wait(40)

        TypeofHomevalue = driver.find_element(By.XPATH,
                                              "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.view.ViewGroup[2]/android.widget.TextView")
        TypeofHomevalue.click()
        print("TypeofHome value")
        driver.implicitly_wait(40)

        Martialstatus = driver.find_element(By.XPATH,
                                            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout[3]/androidx.cardview.widget.CardView/android.widget.LinearLayout/android.widget.Spinner")
        Martialstatus.click()
        print("Martial status")
        driver.implicitly_wait(40)

        Martialstatusvalue = driver.find_element(By.XPATH,
                                                 "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.view.ViewGroup[2]/android.widget.TextView")
        Martialstatusvalue.click()
        print("Martial status value")
        driver.implicitly_wait(40)

        Numberofdependent = driver.find_element(By.XPATH,
                                                "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout[4]/androidx.cardview.widget.CardView/android.widget.LinearLayout/android.widget.Spinner")
        Numberofdependent.click()
        print("Number of dependent")
        driver.implicitly_wait(40)

        Numberofdependentvalue = driver.find_element(By.XPATH,
                                                     "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.view.ViewGroup[2]/android.widget.TextView")
        Numberofdependentvalue.click()
        print("Number of dependent value")
        driver.implicitly_wait(40)

        NumberofdomesticL = driver.find_element(By.XPATH,
                                                "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout[5]/androidx.cardview.widget.CardView/android.widget.LinearLayout/android.widget.Spinner")
        NumberofdomesticL.click()
        print("Number of domestic Labour")
        driver.implicitly_wait(40)

        NumberofdomesticLvalue = driver.find_element(By.XPATH,
                                                     "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.view.ViewGroup[2]/android.widget.TextView")
        NumberofdomesticLvalue.click()
        print("Number of dependent value")
        driver.implicitly_wait(40)

        Familydetails = driver.find_element(By.XPATH,
                                            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout[7]/android.widget.RelativeLayout")
        Familydetails.click()
        print("Family details Next button")
        driver.implicitly_wait(40)

        # Source of income
        Sourceofincome = driver.find_element(By.XPATH,
                                             "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout[1]/androidx.cardview.widget.CardView/android.widget.LinearLayout/android.widget.Spinner")
        Sourceofincome.click()
        print("Source of income")
        driver.implicitly_wait(40)

        Sourceofincomevalue = driver.find_element(By.XPATH,
                                                  "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.view.ViewGroup[2]/android.widget.TextView")
        Sourceofincomevalue.click()
        print("Source of income value")
        driver.implicitly_wait(40)

        Sourceofwealth = driver.find_element(By.XPATH,
                                             "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout[2]/androidx.cardview.widget.CardView/android.widget.LinearLayout/android.widget.Spinner")
        Sourceofwealth.click()
        print("Source of wealth")
        driver.implicitly_wait(40)

        Sourceofwealthvalue = driver.find_element(By.XPATH,
                                                  "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.view.ViewGroup[2]/android.widget.TextView")
        Sourceofwealthvalue.click()
        print("Source of wealth value")
        driver.implicitly_wait(40)

        SourceofincomeNextbutton = driver.find_element(By.XPATH,
                                                       "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout[4]/android.widget.RelativeLayout")
        SourceofincomeNextbutton.click()
        print("Source of income Next button")
        driver.implicitly_wait(40)

        # PEP

        driver.implicitly_wait(40)
        PEPNextbutton = driver.find_element(By.XPATH,
                                            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.RelativeLayout")
        PEPNextbutton.click()
        print(" PEP Next button")

        driver.implicitly_wait(40)
        ConfirmationPEPpopup = driver.find_element(By.XPATH,
                                                   "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.RelativeLayout")
        ConfirmationPEPpopup.click()
        print("Continue Confirmation PEP popup")

        driver.implicitly_wait(40)
        ExpendituresNextbutton = driver.find_element(By.XPATH,
                                                     "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout[4]/android.widget.RelativeLayout")
        ExpendituresNextbutton.click()
        print("Expenditures Next button")

        # EmailAddress---------------------------------------------------------------------------------------------------------------

        EmailAddress = driver.find_element(By.ID, "sa.thelendinghub:id/tvSector")
        # EmailAddress.send_keys("Zudwer213@mailinator.com")
        EmailAddress.send_keys(action_vars.get_email())
        print("EmailAddress")
        driver.implicitly_wait(40)
        EmailNextbutton = driver.find_element(By.XPATH,
                                              "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.RelativeLayout")
        EmailNextbutton.click()

        CPEmailOTP1 = driver.find_element(By.ID, "sa.thelendinghub:id/pin_digit_1")
        CPEmailOTP1.send_keys("0")
        CPEmailOTP2 = driver.find_element(By.ID, "sa.thelendinghub:id/pin_digit_2")
        CPEmailOTP2.send_keys("0")
        CPEmailOTP3 = driver.find_element(By.ID, "sa.thelendinghub:id/pin_digit_3")
        CPEmailOTP3.send_keys("0")
        driver.implicitly_wait(40)
        CPEmailOTP4 = driver.find_element(By.ID, "sa.thelendinghub:id/pin_digit_4")
        CPEmailOTP4.send_keys("0")
        driver.implicitly_wait(40)
        CPEmailOTP5 = driver.find_element(By.ID, "sa.thelendinghub:id/pin_digit_5")
        CPEmailOTP5.send_keys("0")
        driver.implicitly_wait(40)
        CPEmailOTP5 = driver.find_element(By.ID, "sa.thelendinghub:id/pin_digit_6")
        CPEmailOTP5.send_keys("0")
        driver.implicitly_wait(40)

        CompleteProfilebutton = driver.find_element(By.XPATH,
                                                    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.LinearLayout/android.widget.RelativeLayout")
        CompleteProfilebutton.click()
        print("Complete Profile button")
        driver.implicitly_wait(40)

        Thankyouscreen = driver.find_element(By.XPATH,
                                             "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.RelativeLayout")
        Thankyouscreen.click()
        print("Dashboard button")
        driver.implicitly_wait(40)

        driver.close()


    except Exception as e:
        print(f"Error: {e}")


# Function to close the Appium driver
def close_driver(driver):
    driver.quit()
    print("Driver Closed")


# Main program execution
if __name__ == "__main__":
    driver = start_driver()  # Start the driver
    perform_action(driver)  # Perform action (click two buttons)
    time.sleep(5)  # Wait for a few seconds to observe the action
    close_driver(driver)  # Close the driver

    # Find the button by its ID, accessibility ID, or other selectors
    # driver.find_element(By.ID, 'com.jamipartners.thelendinghub:id/buttonRegister').click()  # Replace with actual ID
    # button.click()  # Click the button

    # Optional: Wait to see the result
    # time.sleep(5)

# finally:
#     driver.quit()  # Close the app and end the session
