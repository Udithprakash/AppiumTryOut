from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.common import AppiumOptions
from appium.webdriver.appium_service import AppiumService
import time
 
class DeckerApp:
 
    cap ={
        "devicename": "Samsung",
        "platformName": "Android",
        "automationName": "UiAutomator2",
        "version":"9.0",
        "udid":"emulator-5554",
        "browserName": "chrome",
        "chromedriverExecutable": "C:\Users\2022367\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"
            }
 
def initiate_Driver(self):
 
    #self.appium_service =AppiumService()
    #global appium service
    try:
        global driver
        #driver = webdriver.Remote("http:localhost:4723/wd/hub", self.desired_caps)
        driver = webdriver.Remote("http:localhost:4723/wd/hub", options=AppiumOptions().load_capabilities(self.cap))
        driver.update_settings({"waitForIdleTimeut":500})
    except TypeError:
        print("error: Appium Server is not Working ....")
        self.appium_Service.stop()
 
def launch_Appium_Driver(self):
 
    driver.get("https://www.quest-global.com/")
    time.sleep(15)

 
def docker_logo_validation(self):
    try:
        if driver.find_element(AppiumBy.XPATH, "(//a[@class='navbar-brand-img-fluid])[1]").is_displayed():
            print("kubernets logo is present")
            driver.find_element(AppiumBy.XPATH, "//button[@id='hamburger]").click()
            time.sleep(5)
            driver.find_element(AppiumBy.XPATH, "(//a[text()='Training'])[2]").click()
            time.sleep(20)
    except:
        print("kubernets logo is not present")
 
def close_driver(self):
    driver.quit()
    print("Driver Instance Closed Successfully ....")
    time.sleep(20)
 
 
obj = DeckerApp()
obj.initiate_Driver()
obj.launch_Appium_Driver()
obj.docker_logo_validation()
obj.close_driver()