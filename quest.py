from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.common import AppiumOptions
from appium.webdriver.appium_service import AppiumService
import time
 
class Calculator:
 
    cap = {
  "appium:deviceName": "Samusung",
  "platformName": "Android",
  "appium:automationName": "UiAutomator2",
  "appium:app": "com.google.android.calculator",
  "appium:appActivity": "com.android.calculator2.Calculator"
}
    def initiate_Driver(self):
    
        #self.appium_service =AppiumService()
        #global appium service
        try:
            global driver
            #driver = webdriver.Remote("http:localhost:4723/wd/hub", self.desired_caps)
            driver = webdriver.Remote("http://localhost:4723/wd/hub", options=AppiumOptions().load_capabilities(self.cap))
            driver.update_settings({"waitForIdleTimeut":500})
        except TypeError:
            print("error: Appium Server is not Working ....")
            self.appium_Service.stop()


    def launch_Appium_Driver(self):
    
        driver.get("https://www.quest-global.com/")
        time.sleep(15)


    #click on hamburger menu
        try:
            driver.find_element(AppiumBy.XPATH,"//*[@id='navbar_top']/div/button/span").click()
            time.sleep(5)
            count=len(driver.find_elements(AppiumBy.XPATH,"//*[@id='nav_mobile']/ul/li"))
            for i in range(1,count+1):
                item = driver.find_element(AppiumBy.XPATH,"//*[@id='nav_mobile']/ul/li["+str(i)+"]").text
                print(item)
        except:
            print("test failed")

    def quit_session(self):
        driver.quit()

    
       
obj=Quest()
obj.initiate_Driver()
obj.launch_Appium_Driver()
obj.quit_session()