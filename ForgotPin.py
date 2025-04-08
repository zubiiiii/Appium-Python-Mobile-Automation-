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
        "autoGrantPermissions": True,
        'unicodeKeyboard': False,  # Enable Unicode keyboard
        'resetKeyboard': False,  # Reset keyboard after typing
    }

    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
    return driver

class ActionVariables:
    def __init__(self):
        # Define all variables in the constructor
        self.id_number = '1081383188'  # ID Number variable
        self.cell_number='544639515'
        self.OTP='000000'
    def get_id_number(self):
        return self.id_number

    def get_OTP(self):
        return self.OTP



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
        time.sleep(4)

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

        # time.sleep(12)

        ForgotPinbutton = driver.find_element(By.ID, "sa.thelendinghub:id/tvLbForgetPin")
        ForgotPinbutton.click()
        print("click forgot Pin ")

        driver.implicitly_wait(3)


        # ForgotOTPclick = driver.find_element(By.ID, "sa.thelendinghub:id/pin_digit_1")
        # ForgotOTPclick.click()
        # print("click ")
        # driver.implicitly_wait(40)

        ForgotOTP1 = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.EditText[1]")
        # ForgotOTP1.send_keys("0")
        ForgotOTP1.send_keys(action_vars.get_OTP())
        print("login OTP 000000 ")

        # driver.implicitly_wait(40)

        ForgotOTP2 = driver.find_element(By.ID, "sa.thelendinghub:id/pin_digit_2")
        ForgotOTP2.send_keys("0")
        print("login OTP 2 ")
        driver.implicitly_wait(40)
        ForgotOTP3 = driver.find_element(By.ID, "sa.thelendinghub:id/pin_digit_3")
        ForgotOTP3.send_keys("0")
        print("Login OTP 3 ")
        driver.implicitly_wait(40)
        ForgotOTP4 = driver.find_element(By.ID, "sa.thelendinghub:id/pin_digit_4")
        ForgotOTP4.send_keys("0")
        print("Login OTP 4 ")
        driver.implicitly_wait(40)
        ForgotOTP5 = driver.find_element(By.ID, "sa.thelendinghub:id/pin_digit_5")
        ForgotOTP5.send_keys("0")
        print("Login OTP 5 ")
        driver.implicitly_wait(40)
        ForgotOTP6 = driver.find_element(By.ID, "sa.thelendinghub:id/pin_digit_6")
        ForgotOTP6.send_keys("0")
        print("Login OTP 6 ")

        driver.back()
        driver.implicitly_wait(10)
        continiueloginb111 = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.RelativeLayout")
        continiueloginb111.click()
        print("Submit Code ")

        driver.implicitly_wait(40)
        NewPinCode1 = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.EditText[1]")
        NewPinCode1.send_keys("9")
        print("New Pin Code 1 ")

        driver.implicitly_wait(40)

        NewPinCode2 = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.EditText[2]")
        NewPinCode2.send_keys("8")
        print("New Pin Code 2 ")
        driver.implicitly_wait(40)
        NewPinCode3 = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.EditText[3]")
        NewPinCode3.send_keys("7")
        print("New Pin Code 3 ")
        driver.implicitly_wait(40)
        NewPinCode4 = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.EditText[4]")
        NewPinCode4.send_keys("6")
        print("New Pin Code 4 ")
        driver.implicitly_wait(40)
        NewPinCode5 = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.EditText[5]")
        NewPinCode5.send_keys("5")
        print("New Pin Code 5 ")
        driver.implicitly_wait(40)
        NewPinCode6 = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.EditText[6]")
        NewPinCode6.send_keys("4")
        print("New Pin Code 6 ")

        driver.implicitly_wait(40)
        ConfirmNewPinCode1 = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.EditText[1]")
        ConfirmNewPinCode1.send_keys("9")
        print("Confirm New Pin Code 1 ")
        driver.implicitly_wait(40)
        ConfirmNewPinCode2 = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.EditText[2]")
        ConfirmNewPinCode2.send_keys("8")
        print("Confirm New Pin Code 2 ")
        driver.implicitly_wait(40)
        ConfirmNewPinCode3 = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.EditText[3]")
        ConfirmNewPinCode3.send_keys("7")
        print("Confirm New Pin Code 3 ")
        driver.implicitly_wait(40)
        ConfirmNewPinCode4 = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.EditText[4]")
        ConfirmNewPinCode4.send_keys("6")
        print("Confirm New Pin Code 4 ")
        driver.implicitly_wait(40)
        ConfirmNewPinCode5 = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.EditText[5]")
        ConfirmNewPinCode5.send_keys("5")
        print("Confirm New Pin Code 5 ")
        driver.implicitly_wait(40)
        ConfirmNewPinCode6 = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.EditText[6]")
        ConfirmNewPinCode6.send_keys("4")
        print("Confirm New Pin Code 6 ")
        driver.implicitly_wait(40)
        Savenewpincode = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[3]/android.widget.RelativeLayout")
        Savenewpincode.click()
        driver.implicitly_wait(10)


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
