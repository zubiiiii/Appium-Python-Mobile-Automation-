import self
from appium import webdriver
import time
# from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction
# from selenium.webdriver.common.action_chains import ActionChains



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
        self.id_number = '1081383117'  # ID Number variable
        self.cell_number='544639515'
        self.email='zubaiwerdr@mailinator.com'
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
        time.sleep(1)

        Languagestartenlish=driver.find_element(By.ID, 'sa.thelendinghub:id/btnEnglish')  # Button 1 ID
        Languagestartenlish.click()  # Click the first button
        print("Language start english")

        # driver.implicitly_wait(7)
        # Finding and clicking the second button
        onboarding1 = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.RelativeLayout")  # Button 2 ID
        onboarding1.click()  # Click the second button
        print("Premium fintech platform of Saudia Arabic")

        driver.implicitly_wait(7)
        onboarding2 = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.RelativeLayout")  # Button 2 ID
        onboarding2.click()  # Click the second button
        print("Investmet at its simplest")

        driver.implicitly_wait(7)
        onboarding3 = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.RelativeLayout")  # Button 2 ID
        onboarding3.click()  # Click the second button
        print("Apply for financing is a breeze")

        driver.implicitly_wait(7)
        onboarding4 = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.RelativeLayout")  # Button 2 ID
        onboarding4.click()  # Click the second button
        print("Button 2 Clicked")

        driver.implicitly_wait(7)

        loginbluescreen = driver.find_element(By.ID,"sa.thelendinghub:id/btnLogin")
        loginbluescreen.click()  # Click the second button
        print("login button validation")

        driver.implicitly_wait(7)
        enterID = driver.find_element(By.ID, "sa.thelendinghub:id/editIdNumber")
        enterID.send_keys(action_vars.get_id_number())  # Click the second button
        print("inserting id")

        loginbluescreen = driver.find_element(By.ID,"sa.thelendinghub:id/btnLogin")
        loginbluescreen.click()  # Click the second button
        print("submit button ")
        driver.implicitly_wait(7)


        registernow=driver.find_element(By.ID,'sa.thelendinghub:id/imgBtnRegister')
        registernow.click()
        print("register now button")
        driver.implicitly_wait(7)

        # Selectype=driver.find_element(By.ID,'sa.thelendinghub:id/constraintBorrower')
        # Selectype.click(action_vars.get_Lender())

        time.sleep(7)
        # driver.implicitly_wait(40)
        Proceed=driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout/android.widget.RelativeLayout")
        Proceed.click()
        print("Proceed to Verification button ")

        # time.sleep(5)
        driver.implicitly_wait(40)
        addphone=driver.find_element(By.ID,"sa.thelendinghub:id/editCellNumber")
        addphone.send_keys(action_vars.get_cell_number())
        print("cell number ")

        # driver.implicitly_wait(7)
        # selectdob=driver.find_element(By.ID,'sa.thelendinghub:id/editDob')
        # selectdob.send_keys("october 28, 1990")
        # print("select month ")
        # time.sleep(20)

        # actions = ActionChains(driver)
        driver.implicitly_wait(40)
        ViewCalendar=driver.find_element(By.ID,"sa.thelendinghub:id/imageViewCalendar")
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
        Proceed=driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout[5]/android.widget.RelativeLayout")
        Proceed.click()
        print("Proceed to Verification button ")
        driver.implicitly_wait(40)


        RegistrationOTP1=driver.find_element(By.ID,"sa.thelendinghub:id/pin_digit_1")
        RegistrationOTP1.send_keys("0")
        print("OTP digit 1 ")

        RegistrationOTP2=driver.find_element(By.ID,"sa.thelendinghub:id/pin_digit_2")
        RegistrationOTP2.send_keys("0")
        print("OTP digit 2 ")

        RegistrationOTP3=driver.find_element(By.ID,"sa.thelendinghub:id/pin_digit_3")
        RegistrationOTP3.send_keys("0")
        print("OTP digit 3 ")

        RegistrationOTP4=driver.find_element(By.ID,"sa.thelendinghub:id/pin_digit_4")
        RegistrationOTP4.send_keys("0")
        print("OTP digit 4 ")

        RegistrationOTP5=driver.find_element(By.ID,"sa.thelendinghub:id/pin_digit_5")
        RegistrationOTP5.send_keys("0")
        print("OTP digit 5 ")

        RegistrationOTP6=driver.find_element(By.ID,"sa.thelendinghub:id/pin_digit_6")
        RegistrationOTP6.send_keys("00")
        print("OTP digit 6 ")
        #
        driver.implicitly_wait(40)
        OTPVerifyCredentials = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.RelativeLayout")
        OTPVerifyCredentials.click()
        print("OTPVerifyCredentials ")

        driver.implicitly_wait(40)

        RegisterSETPIN9=driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.EditText[1]")
        RegisterSETPIN9.send_keys("9")
        print("New Pin Code 9 ")

        driver.implicitly_wait(40)

        RegisterSETPIN8=driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.EditText[2]")
        RegisterSETPIN8.send_keys("8")
        print("Set Pin Code 8 ")

        RegisterSETPIN7=driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.EditText[3]")
        RegisterSETPIN7.send_keys("7")
        print("Set Pin Code 7")

        RegisterSETPIN6=driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.EditText[4]")
        RegisterSETPIN6.send_keys("6")
        print("New Pin Code 6")

        RegisterSETPIN5=driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.EditText[5]")
        RegisterSETPIN5.send_keys("5")
        print("Set Pin Code 5")

        RegisterSETPIN6=driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.EditText[6]")
        RegisterSETPIN6.send_keys("4")
        print("Set Pin Code 4")


        driver.implicitly_wait(40)
        RegisterConfirmnewPIN1=driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.EditText[1]")
        RegisterConfirmnewPIN1.send_keys("9")
        print("New Pin Code 9")

        RegisterConfirmnewPIN2=driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.EditText[2]")
        RegisterConfirmnewPIN2.send_keys("8")
        print("New Pin Code 8")

        RegisterConfirmnewPIN3=driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.EditText[3]")
        RegisterConfirmnewPIN3.send_keys("7")
        print("New Pin Code 7")

        RegisterConfirmnewPIN4=driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.EditText[4]")
        RegisterConfirmnewPIN4.send_keys("6")
        print("New Pin Code 6")

        RegisterConfirmnewPIN5 = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.EditText[5]")
        RegisterConfirmnewPIN5.send_keys("5")
        print("New Pin Code 5")


        RegisterConfirmnewPIN6 = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.EditText[6]")
        RegisterConfirmnewPIN6.send_keys("4")
        print("New Pin Code 4")

        driver.implicitly_wait(40)
        # checkboxTandC = driver.find_element(By.ID,"sa.thelendinghub:id/tvTermsConditions")
        # checkboxTandC.click()
        # print("checkbox Terms and Condition View")
        # time.sleep(10)
        #
        # driver.implicitly_wait(40)
        # cancellbutton = driver.find_element(By.ID,"sa.thelendinghub:id/imageView")
        # cancellbutton.click()
        # print("Cancell button")
        #
        # driver.implicitly_wait(40)
        # checkboxTandC = driver.find_element(By.ID,"sa.thelendinghub:id/textViewPrivacyPolicy")
        # checkboxTandC.click()
        # print("checkbox Privacy Policy View")
        # time.sleep(10)
        #
        # driver.implicitly_wait(40)
        # cancellbutton = driver.find_element(By.ID,"sa.thelendinghub:id/imageView")
        # cancellbutton.click()
        # print("Cancell button")

        driver.implicitly_wait(40)
        checkboxTandC = driver.find_element(By.ID,"sa.thelendinghub:id/checkBox")
        checkboxTandC.click()
        print("checkbox Terms and Condition")

        driver.implicitly_wait(40)
        checkboxPandP = driver.find_element(By.ID,"sa.thelendinghub:id/checkBoxPrivacyPolicy")
        checkboxPandP.click()
        print("checkbox privacy and policy")


        driver.implicitly_wait(40)
        Completeregistrationbutton = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout[3]/android.widget.RelativeLayout")
        Completeregistrationbutton.click()
        print("Complete registration button")

        driver.implicitly_wait(10)

        Completeregistrationcontinue = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.RelativeLayout")
        Completeregistrationcontinue.click()
        print("after Complete registration button Continue")
        driver.implicitly_wait(40)

        Completeprofiletile= driver.find_element(By.ID,"sa.thelendinghub:id/cardviewCompleteProfile")
        Completeprofiletile.click()
        print("click Complete profile tile")
        driver.implicitly_wait(40)

        PersnoldetailNextbutton= driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout[1]/android.widget.RelativeLayout")
        PersnoldetailNextbutton.click()
        print("Persnal detail Next button")
        driver.implicitly_wait(40)


        #occupation and Employer
        Sector= driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout[1]/androidx.cardview.widget.CardView/android.widget.LinearLayout/android.widget.Spinner")
        Sector.click()
        print("click sector")
        driver.implicitly_wait(40)

        Sectorvalue = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.view.ViewGroup[2]/android.widget.TextView")
        Sectorvalue.click()
        print("Sector Value")
        driver.implicitly_wait(40)

        Jobtitle= driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout[2]/androidx.cardview.widget.CardView/android.widget.LinearLayout/android.widget.Spinner")
        Jobtitle.click()
        print("click job title")
        driver.implicitly_wait(40)

        Jobtitlevalue = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.view.ViewGroup[2]/android.widget.TextView")
        Jobtitlevalue.click()
        print("Jobtitlevalue")
        driver.implicitly_wait(40)

        Natureoffield= driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout[3]/androidx.cardview.widget.CardView/android.widget.LinearLayout/android.widget.Spinner")
        Natureoffield.click()
        print("nature of field click")
        driver.implicitly_wait(40)

        Natureoffieldvalue = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.view.ViewGroup[2]/android.widget.TextView")
        Natureoffieldvalue.click()
        print("nature of field value")
        driver.implicitly_wait(40)

        Education= driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout[4]/androidx.cardview.widget.CardView/android.widget.LinearLayout/android.widget.Spinner")
        Education.click()
        print("Education click")
        driver.implicitly_wait(40)

        Educationvalue = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.view.ViewGroup[2]/android.widget.TextView")
        Educationvalue.click()
        print("Education value")
        driver.implicitly_wait(40)

        occupationandEmployerNextbutton = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout[6]/android.widget.RelativeLayout")
        occupationandEmployerNextbutton.click()
        print("occupation and Employer Next button")
        driver.implicitly_wait(40)

        #Family details
        Homeownership = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout[1]/androidx.cardview.widget.CardView/android.widget.LinearLayout/android.widget.Spinner")
        Homeownership.click()
        print("Homeownership")
        driver.implicitly_wait(40)

        Homeownershipvalue = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.view.ViewGroup[2]/android.widget.TextView")
        Homeownershipvalue.click()
        print("Homeownership value")
        driver.implicitly_wait(40)

        TypeofHome = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout[2]/androidx.cardview.widget.CardView/android.widget.LinearLayout/android.widget.Spinner")
        TypeofHome.click()
        print("TypeofHome")
        driver.implicitly_wait(40)

        TypeofHomevalue = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.view.ViewGroup[2]/android.widget.TextView")
        TypeofHomevalue.click()
        print("TypeofHome value")
        driver.implicitly_wait(40)

        Martialstatus = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout[3]/androidx.cardview.widget.CardView/android.widget.LinearLayout/android.widget.Spinner")
        Martialstatus.click()
        print("Martial status")
        driver.implicitly_wait(40)

        Martialstatusvalue = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.view.ViewGroup[2]/android.widget.TextView")
        Martialstatusvalue.click()
        print("Martial status value")
        driver.implicitly_wait(40)

        Numberofdependent = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout[4]/androidx.cardview.widget.CardView/android.widget.LinearLayout/android.widget.Spinner")
        Numberofdependent.click()
        print("Number of dependent")
        driver.implicitly_wait(40)

        Numberofdependentvalue = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.view.ViewGroup[2]/android.widget.TextView")
        Numberofdependentvalue.click()
        print("Number of dependent value")
        driver.implicitly_wait(40)

        NumberofdomesticL = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout[5]/androidx.cardview.widget.CardView/android.widget.LinearLayout/android.widget.Spinner")
        NumberofdomesticL.click()
        print("Number of domestic Labour")
        driver.implicitly_wait(40)


        NumberofdomesticLvalue = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.view.ViewGroup[2]/android.widget.TextView")
        NumberofdomesticLvalue.click()
        print("Number of dependent value")
        driver.implicitly_wait(40)

        Familydetails = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout[7]/android.widget.RelativeLayout")
        Familydetails.click()
        print("Family details Next button")
        driver.implicitly_wait(40)


        #Source of income
        Sourceofincome = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout[1]/androidx.cardview.widget.CardView/android.widget.LinearLayout/android.widget.Spinner")
        Sourceofincome.click()
        print("Source of income")
        driver.implicitly_wait(40)

        Sourceofincomevalue = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.view.ViewGroup[2]/android.widget.TextView")
        Sourceofincomevalue.click()
        print("Source of income value")
        driver.implicitly_wait(40)

        Sourceofwealth = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout[2]/androidx.cardview.widget.CardView/android.widget.LinearLayout/android.widget.Spinner")
        Sourceofwealth.click()
        print("Source of wealth")
        driver.implicitly_wait(40)

        Sourceofwealthvalue = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.view.ViewGroup[2]/android.widget.TextView")
        Sourceofwealthvalue.click()
        print("Source of wealth value")
        driver.implicitly_wait(40)

        SourceofincomeNextbutton = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout[4]/android.widget.RelativeLayout")
        SourceofincomeNextbutton.click()
        print("Source of income Next button")
        driver.implicitly_wait(40)


        #PEP

        driver.implicitly_wait(40)
        PEPNextbutton = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.RelativeLayout")
        PEPNextbutton.click()
        print(" PEP Next button")

        driver.implicitly_wait(40)
        ConfirmationPEPpopup = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.RelativeLayout")
        ConfirmationPEPpopup.click()
        print("Continue Confirmation PEP popup")


        driver.implicitly_wait(40)
        ExpendituresNextbutton = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout[4]/android.widget.RelativeLayout")
        ExpendituresNextbutton.click()
        print("Expenditures Next button")


        #EmailAddress---------------------------------------------------------------------------------------------------------------

        EmailAddress = driver.find_element(By.ID,"sa.thelendinghub:id/tvSector")
        # EmailAddress.send_keys("Zudwer213@mailinator.com")
        EmailAddress.send_keys(action_vars.get_email())
        print("EmailAddress")
        driver.implicitly_wait(40)
        EmailNextbutton = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.RelativeLayout")
        EmailNextbutton.click()


        CPEmailOTP1 = driver.find_element(By.ID,"sa.thelendinghub:id/pin_digit_1")
        CPEmailOTP1.send_keys("0")
        CPEmailOTP2 = driver.find_element(By.ID,"sa.thelendinghub:id/pin_digit_2")
        CPEmailOTP2.send_keys("0")
        CPEmailOTP3 = driver.find_element(By.ID,"sa.thelendinghub:id/pin_digit_3")
        CPEmailOTP3.send_keys("0")
        driver.implicitly_wait(40)
        CPEmailOTP4 = driver.find_element(By.ID,"sa.thelendinghub:id/pin_digit_4")
        CPEmailOTP4.send_keys("0")
        driver.implicitly_wait(40)
        CPEmailOTP5 = driver.find_element(By.ID,"sa.thelendinghub:id/pin_digit_5")
        CPEmailOTP5.send_keys("0")
        driver.implicitly_wait(40)
        CPEmailOTP5 = driver.find_element(By.ID,"sa.thelendinghub:id/pin_digit_6")
        CPEmailOTP5.send_keys("0")
        driver.implicitly_wait(40)

        CompleteProfilebutton = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.LinearLayout/android.widget.RelativeLayout")
        CompleteProfilebutton.click()
        print("Complete Profile button")
        driver.implicitly_wait(40)

        Thankyouscreen = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.RelativeLayout")
        Thankyouscreen.click()
        print("Dashboard button")
        driver.implicitly_wait(40)

        Applyforfinancingbutton = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout")
        Applyforfinancingbutton.click()
        print("Apply for financing button")
        driver.implicitly_wait(40)

        Proceedbutton = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout/android.widget.RelativeLayout")
        Proceedbutton.click()
        print("Proceed button")
        driver.implicitly_wait(40)

        SimahDisclaimer = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.RelativeLayout")
        SimahDisclaimer.click()
        print("Simah Disclaimer I agree")
        driver.implicitly_wait(40)

        PersnoldetailNextbutton = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout[1]/android.widget.RelativeLayout")
        PersnoldetailNextbutton.click()
        print("Persnol detail Next button")
        driver.implicitly_wait(40)

        occupationandEmployerNextbutton = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout[6]/android.widget.RelativeLayout")
        occupationandEmployerNextbutton.click()
        print("occupation and Employer Next button")
        driver.implicitly_wait(40)

        Familydetails = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout[7]/android.widget.RelativeLayout")
        Familydetails.click()
        print("Family details Next button")
        driver.implicitly_wait(40)

        SourceofincomeNextbutton = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout[4]/android.widget.RelativeLayout")
        SourceofincomeNextbutton.click()
        print("Source of income Next button")
        driver.implicitly_wait(40)

        PEPNextbutton = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.RelativeLayout")
        PEPNextbutton.click()
        print(" PEP Next button")

        ConfirmationPEPpopup = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.RelativeLayout")
        ConfirmationPEPpopup.click()
        print("Continue Confirmation PEP popup")

        driver.implicitly_wait(10)
        ExpendituresNextbutton = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout[4]/android.widget.RelativeLayout")
        ExpendituresNextbutton.click()
        print("Expenditures Next button")


        driver.implicitly_wait(25)
        RequiredFinancingAmount = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.SeekBar")
        RequiredFinancingAmount.click()
        print("Required Financing Amount")

        driver.implicitly_wait(40)
        RequiredFinancingduration = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.SeekBar")
        RequiredFinancingduration.click()
        print("Required Financing Duration")

        driver.implicitly_wait(40)
        Reasonforfinancing = driver.find_element(By.ID,"sa.thelendinghub:id/spinner_sector")
        Reasonforfinancing.click()
        print("Reason for financing")

        driver.implicitly_wait(40)
        Reasonforfinancingvalue = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.view.ViewGroup[2]/android.widget.TextView")
        Reasonforfinancingvalue.click()
        print("Reason for financing value")

        driver.implicitly_wait(40)
        RequiredFinancingdetailnextbutton = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout[5]/android.widget.RelativeLayout")
        RequiredFinancingdetailnextbutton.click()
        print("Required Financing detail Next buton")

        driver.implicitly_wait(40)
        action = TouchAction(driver)
        action.press(x=500, y=1500).move_to(x=500, y=500).release().perform()

        driver.implicitly_wait(40)
        Confirmbutton = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.RelativeLayout")
        Confirmbutton.click()
        print("Confirm button")

        driver.implicitly_wait(40)
        acceptofferbutton = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.RelativeLayout")
        acceptofferbutton.click()
        print("accept offer button")

        driver.implicitly_wait(40)
        acceptofferbuttonyes = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[1]/android.widget.RelativeLayout")
        acceptofferbuttonyes.click()
        print("accept offer button yes,proceed")

        driver.implicitly_wait(40)
        thankyouscreendashboardbutton = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.LinearLayout/android.widget.RelativeLayout")
        thankyouscreendashboardbutton.click()
        print("thank you screen dashboard button")
        driver.implicitly_wait(40)

        navigation = driver.find_element(By.ID,"sa.thelendinghub:id/imageViewNav")
        navigation.click()
        print("navigation")
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