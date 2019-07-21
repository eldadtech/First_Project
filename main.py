# Automating "BuyME" Website Project
# Goal : Sanity Test
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
import logging
import os
import random

PROJECT_PATH = (os.getcwd())  # get project path
LOGGER = logging.getLogger('Error')  # initiate logger


def create_random_email():  # Create random email to subscribe
    email = "some_email"
    for x in range(5):
        email += str(random.randint(1, 101))
    email += "@gmail.com"
    return email


# Open buyme.co.il page with chrome driver
def open_site():
    # get chrome driver
    driver = webdriver.Chrome(executable_path="C:\\Users\\Eldad\\Downloads\\chromedriver_win32\\chromedriver.exe")
    driver.implicitly_wait(5)
    # Enter the Site
    driver.get("http://www.buyme.co.il")
    driver.maximize_window()
    return driver


# Open login page
def login(driver):
    # Click Login/Subscribe
    login_button = driver.find_element_by_xpath("//div[@id='ember591']//li[3]")
    driver.execute_script("arguments[0].click();", login_button)


# Close and quit selenium driver
def end_automation(driver):
    time.sleep(5)  # just to view the result before closing
    driver.close()
    driver.quit()


def subscribe_automation():
    try:
        # open site
        driver = open_site()
        # Click Login/Subscribe
        login(driver)
        # Click Subscribe Link
        driver.find_element_by_xpath("//span[@class='text-btn'][contains(.,'להרשמה')]").click()
        # Enter first Name
        driver.find_element_by_xpath("//input[@placeholder='שם פרטי']").send_keys("eldad")
        # Enter email
        email = create_random_email()
        driver.find_element_by_xpath("//input[@placeholder='מייל']").send_keys(email)
        # Enter Password
        driver.find_element_by_xpath("//input[@placeholder='סיסמה']").send_keys("P@ssw0rd")
        # Confirm Password
        driver.find_element_by_xpath("//input[@placeholder='אימות סיסמה']").send_keys("P@ssw0rd")
        # Confirm Agree radio button
        agree_button = driver.find_element_by_xpath("(//input[@type='checkbox'])[1]")
        driver.execute_script("arguments[0].click()", agree_button)
        # Click subscribe button
        driver.find_element_by_xpath("//button[contains(@class,'ui-btn orange large')]").click()
        time.sleep(10)
    except BaseException as e:  # catch error and print it
        LOGGER.error("failed " + str(e))
    finally:
        end_automation(driver)


def buy_me_automation():
    try:
        # open site
        driver = open_site()
        # Click Login/Subscribe
        login(driver)
        # Login to the site
        login_name = driver.find_element_by_xpath("(//input[contains(@type,'email')])[1]")
        login_name.send_keys("eldadtech@gmail.com")
        login_name = driver.find_element_by_xpath("//input[contains(@type,'password')]")
        login_name.send_keys("Eldad1234")
        login_name = driver.find_element_by_xpath("// button[ @class ='ui-btn orange large']")
        login_name.click()
        time.sleep(1)  # time to close the popup window

        # Pick a price
        price_point = driver.find_element_by_link_text("סכום")
        price_point.click()
        driver.find_element_by_xpath("//li[@data-option-array-index='3']").click()
        # Pick a area
        driver.find_element_by_link_text("אזור").click()
        driver.find_element_by_xpath("//li[@data-option-array-index='2']").click()
        # Pick a category
        driver.find_element_by_link_text("קטגוריה").click()
        driver.find_element_by_xpath("//li[@data-option-array-index='4']").click()
        # Press the search button
        choice_p = driver.find_elements_by_xpath("//input[@id='ember721']")
        # pick a business
        choice_p[0].send_keys("פפריקה")
        driver.find_element_by_link_text("תמצאו לי מתנה").click()
        driver.find_element_by_xpath('//a[@href="https://buyme.co.il/supplier/1135477"]').click()
        # type a price
        price_point = driver.find_element_by_xpath("//input[@placeholder='מה הסכום?']")
        price_point.send_keys("345")
        price_point.send_keys(Keys.ENTER)
        # Press radio button
        driver.find_element_by_xpath("(//span[@class='circle'])[1]").click()
        # Receiver Name
        input_data = driver.find_element_by_xpath(
            "//input[contains(@data-parsley-required-message,'מי הזוכה המאושר?')]")
        input_data.send_keys("ישראל")
        # enter a blessing
        blessing = driver.find_element_by_xpath("//label[@class='ember-view ui-field ui-textarea']")
        blessing.send_keys(Keys.CONTROL + "a")
        blessing.send_keys(Keys.DELETE)
        blessing.send_keys("שהכל ניהיה בדברו")
        # upload picture
        driver.find_element_by_name("fileUpload").send_keys(PROJECT_PATH + "\pic.png")
        # pick the event
        driver.find_element_by_link_text('לאיזה אירוע?').click()
        driver.find_element_by_xpath("//li[@data-option-array-index='3']").click()
        # Press after payement radio button
        after_payment = driver.find_element_by_xpath("//div[@id='step-2-later-options']")
        driver.execute_script("arguments[0].click();", after_payment)
        # Pick Email option
        element = driver.find_element_by_xpath("//span[contains(text(),'במייל')]")
        driver.execute_script("arguments[0].click();", element)
        # Enter Address email and save
        mail_address = driver.find_element_by_xpath("//input[@placeholder='כתובת המייל של מקבל/ת המתנה']")
        mail_address.send_keys("eldadtech@gmail.com")
        mail_address.send_keys(Keys.ENTER)

    except BaseException as e:  # catch error and print it
        LOGGER.error("failed " + str(e))
    finally:
        end_automation(driver)


if __name__ == '__main__':
    # print("Welcome to the automation project")
    # print("Please enter your choice")
    # print("click 1 to run subscribe automation")
    # print("click 1 to run buy process automation automation")
    # choice = input("What are you decide ?")
    # print(choice)
    # if choice == "1":
        subscribe_automation()
#     if choice == "2":
#         buy_me_automation()
#     else:
#         print("Error Input")
#
# print("End Automation")
