from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.common import AppiumOptions
from appium.webdriver.appium_service import AppiumService
import time

class CalculatorApp:
 
    cap = {
  "appium:deviceName": "Samusung",
  "platformName": "Android",
  "appium:automationName": "UiAutomator2",
  "appium:appPackage": "com.google.android.calculator",
  "appium:appActivity": "com.android.calculator2.Calculator"
}

    def initiate_Driver(self):
        #self.apppium_service = AppiumService()
        #global appium_service
       
        try:
            global driver
            driver = webdriver.Remote("http://localhost:4723/wd/hub", options=AppiumOptions().load_capabilities(self.cap))
            driver.update_settings({"waitForIdleTimeout": 500})
        except TypeError:
            print("Error:Appium server not working ...")


    def Calculator_do_addition(self):
        try:
            driver.find_element(AppiumBy.ID,"com.google.android.calculator:id/digit_9").click()
            time.sleep(2)
            driver.find_element(AppiumBy.ID,"com.google.android.calculator:id/op_add").click()
            time.sleep(2)
            driver.find_element(AppiumBy.ID,"com.google.android.calculator:id/digit_9").click()
            time.sleep(2)
            driver.find_element(AppiumBy.ID,"com.google.android.calculator:id/eq").click()
            time.sleep(2)
            result=driver.find_element(AppiumBy.ID,"com.google.android.calculator:id/result_final").text

            if int(result)==18:
                print("The result is expected as:"+result)

        except:
            print("Calculator is not working as expected ")


        time.sleep(5)

obj=CalculatorApp()
obj.initiate_Driver()
obj.Calculator_do_addition()        