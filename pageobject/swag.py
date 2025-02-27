from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
import time



def do_scroll(driver):
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(509, 2088)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.move_to_location(533, 293)
    actions.w3c_actions.pointer_action.release()
    actions.perform()
    time.sleep(5)
    
def username():
    return "//android.widget.EditText[@content-desc='test-Username']"
def password():
    return "//android.widget.EditText[@content-desc='test-Password']"
def login():
    return "//android.view.ViewGroup[@content-desc='test-LOGIN']"
def addcart1():
    return "(//android.widget.TextView[@text='ADD TO CART'])[1]"
def addcart2():
    return "//android.widget.TextView[@text='ADD TO CART']"
def validatecart():
    return "//android.widget.TextView[@text='2']"
def cart_count():
    return "//android.widget.TextView[@text='REMOVE']"
def check_out():
    return "//android.view.ViewGroup[@content-desc='test-Cart']/android.view.ViewGroup/android.view.ViewGroup"
def clicheck():
    return "//android.widget.TextView[@text='CHECKOUT']"
def firstname():

    return "//android.widget.EditText[@content-desc='test-First Name']"

def lastname():
    return "//android.widget.EditText[@content-desc='test-Last Name']"
def pin():
    return "//android.widget.EditText[@content-desc='test-Zip/Postal Code']"

def continueclick():
    return "//android.widget.TextView[@text='CONTINUE']"
def finish():
    return "//android.view.ViewGroup[@content-desc='test-FINISH']"

def item_count():
        return "//android.widget.TextView[@content-desc='test-Item title']"
 
def print_item(i):
        return "(//android.widget.TextView[@content-desc='test-Item title'])["+str(i)+"]"
