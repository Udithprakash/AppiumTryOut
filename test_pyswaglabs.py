import pytest
import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
# from appium.webdriver.appium_service import AppiumService
import time
from pageobject import swag

@pytest.mark.usefixtures("launch_app")
class Test_saucelab:
    def test_abcapp(self,read_json):
        try:
            self.driver.find_element(AppiumBy.XPATH,swag.username()).send_keys(read_json["username"])
            self.driver.find_element(AppiumBy.XPATH,swag.password()).send_keys(read_json["password"])
            self.driver.find_element(AppiumBy.XPATH,swag.login()).click()
            time.sleep(5)
        except:
            print("there is an issue in Login")

            count = len(self.driver.find_elements(AppiumBy.XPATH,swag.item_count()))
            for i in range(1,count+1):
                item = self.driver.find_element(AppiumBy.XPATH,swag.print_item(i)).text
                print(item)



    def test_add_cart(self):
        try:
            self.driver.find_element(AppiumBy.XPATH,swag.addcart1()).click()
            time.sleep(4)
            self.driver.find_element(AppiumBy.XPATH,swag.addcart2()).click()
            time.sleep(5)
        except:
            print("add to cart issue")

    def test_validate_cart(self):
        if self.driver.find_element(AppiumBy.XPATH,swag.validatecart()).is_displayed:
            print("cart validatd")
        else:
            print("not validated")

    def test_cart_count(self):
        count=len(self.driver.find_elements(AppiumBy.XPATH,swag.cart_count()))
        
        print("the number of cart items,",count)
        time.sleep(5)

    def test_checkout(self,read_json):
        self.driver.find_element(AppiumBy.XPATH,swag.check_out()).click()
        time.sleep(5)

        swag.do_scroll(self.driver)

        self.driver.find_element(AppiumBy.XPATH,swag.clicheck()).click()

        time.sleep(5)
        self.driver.find_element(AppiumBy.XPATH,swag.firstname()).send_keys(read_json["firstname"])
        time.sleep(5)
        self.driver.find_element(AppiumBy.XPATH,swag.lastname()).send_keys(read_json["lastname"])
        time.sleep(5)
        self.driver.find_element(AppiumBy.XPATH,swag.pin()).send_keys(read_json["pin"])

        time.sleep(5)
        self.driver.find_element(AppiumBy.XPATH,swag.continueclick()).click()	
        time.sleep(5)
        swag.do_scroll(self.driver)
        self.driver.find_element(AppiumBy.XPATH,swag.finish()).click()
        






    
