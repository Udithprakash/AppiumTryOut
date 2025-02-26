from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.common import AppiumOptions
from appium.webdriver.appium_service import AppiumService
import time

from reusable import do_scroll

 
class Swaglabs:
 
    
    cap = {
            "appium:deviceName": "Samusung",
            "platformName": "Android",
            "appium:automationName": "UiAutomator2",
            "appium:app": "C:\\Users\\2022367\\Downloads\\Android.SauceLabs.Mobile.Sample.app.2.7.1.apk",
            "appium:appWaitActivity": "com.swaglabsmobileapp.MainActivity"
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

    def launch_app(self):
        try:
            driver.find_element(AppiumBy.XPATH,"//android.widget.EditText[@content-desc='test-Username']").send_keys("standard_user")
            time.sleep(5)
            driver.find_element(AppiumBy.XPATH,"//android.widget.EditText[@content-desc='test-Password']").send_keys("secret_sauce")
            time.sleep(5)
            driver.find_element(AppiumBy.XPATH,"//android.view.ViewGroup[@content-desc='test-LOGIN']").click()
            time.sleep(5)
        except:
            print("there is an issue in Login")

    def add_cart(self):
        try:
            driver.find_element(AppiumBy.XPATH,"(//android.widget.TextView[@text='ADD TO CART'])[1]").click()
            time.sleep(4)
            driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='ADD TO CART']").click()
            time.sleep(5)
        except:
            print("add to cart issue")

    def validate_cart(self):
        if driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='2']").is_displayed:
            print("cart validatd")
        else:
            print("not validated")

    def cart_count(self):
        count=len(driver.find_elements(AppiumBy.XPATH,"//android.widget.TextView[@text='REMOVE']"))
       
        print("the number of cart items,",count)
        time.sleep(5)

    def checkout(self):
        driver.find_element(AppiumBy.XPATH,"//android.view.ViewGroup[@content-desc='test-Cart']/android.view.ViewGroup/android.view.ViewGroup").click()
        time.sleep(5)
        do_scroll(driver)

        driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='CHECKOUT']").click()
    
        time.sleep(5)
        driver.find_element(AppiumBy.XPATH,"//android.widget.EditText[@content-desc='test-First Name']").send_keys("udith")
        time.sleep(5)
        driver.find_element(AppiumBy.XPATH,"//android.widget.EditText[@content-desc='test-Last Name']").send_keys("prakash")
        time.sleep(5)
        driver.find_element(AppiumBy.XPATH,"//android.widget.EditText[@content-desc='test-Zip/Postal Code']").send_keys("670007")

        time.sleep(5)
        driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='CONTINUE']").click()	
        time.sleep(5)
        do_scroll(driver)
        driver.find_element(AppiumBy.XPATH,"//android.view.ViewGroup[@content-desc='test-FINISH']").click()
        






    def quit_session(self):
        driver.quit()

obj=Swaglabs()
obj.initiate_Driver()
obj.launch_app()
obj.add_cart()
obj.validate_cart()
obj.cart_count()
obj.checkout()
obj.quit_session()


	

            