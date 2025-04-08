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
        self.id_number = '1081383117'  # ID Number variable
        self.cell_number='544639515'
    def get_id_number(self):
        return self.id_number

    def get_cell_number(self):
        return self.cell_number


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
        time.sleep(3)

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

        LoginOTPverifycredentials = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.RelativeLayout")
        LoginOTPverifycredentials.click()
        driver.implicitly_wait(10)


        Navigationclick= driver.find_element(By.ID,"sa.thelendinghub:id/imageViewNav")
        Navigationclick.click()
        # time.sleep(6000)

        Setting = driver.find_element(By.ID, "sa.thelendinghub:id/settings")
        Setting.click()

        Deactivateaccount = driver.find_element(By.ID, "sa.thelendinghub:id/deactivate")
        Deactivateaccount.click()

        Deactivateaccountpopup = driver.find_element(By.ID, "sa.thelendinghub:id/btnLogout")
        Deactivateaccountpopup.click()

        DeactivateaccountpopupOK = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.RelativeLayout")
        DeactivateaccountpopupOK.click()

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
