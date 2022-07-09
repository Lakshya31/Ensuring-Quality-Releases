# #!/usr/bin/env python
from datetime import datetime, timezone
import traceback
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as ChromeOptions


# Start the browser and login with standard_user
def login(user, password):
    try:
        print('Starting the browser...')
        # --uncomment when running in Azure DevOps.
        options = ChromeOptions()
        options.add_argument("--headless")
        global driver
        driver = webdriver.Chrome(options=options)
        # driver = webdriver.Chrome()
        print(datetime.now(timezone.utc).strftime(
            "%Y-%m-%d %H:%M:%S  "), 'Browser started successfully. Navigating to the demo page to login.')
        driver.get('https://www.saucedemo.com/')

        # Waiting for Page Load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@id='user-name']"))
        )

        # Entering Username
        print(datetime.now(timezone.utc).strftime(
            "%Y-%m-%d %H:%M:%S  "), 'Finding Username Input Box')
        username_input_box = driver.find_element(
            By.XPATH, "//input[@id='user-name']")
        print(datetime.now(timezone.utc).strftime(
            "%Y-%m-%d %H:%M:%S  "), 'Entering Username in Input Box')
        username_input_box.send_keys(user)
        print(datetime.now(timezone.utc).strftime(
            "%Y-%m-%d %H:%M:%S  "), 'Entered Username in Input Box!')

        # Entering Password
        print(datetime.now(timezone.utc).strftime(
            "%Y-%m-%d %H:%M:%S  "), 'Finding Password Input Box')
        password_input_box = driver.find_element(
            By.XPATH, "//input[@id='password']")
        print(datetime.now(timezone.utc).strftime(
            "%Y-%m-%d %H:%M:%S  "), 'Entering Password in Input Box')
        password_input_box.send_keys(password)
        print(datetime.now(timezone.utc).strftime(
            "%Y-%m-%d %H:%M:%S  "), 'Entered Password in Input Box!')

        # Click Login
        print(datetime.now(timezone.utc).strftime(
            "%Y-%m-%d %H:%M:%S  "), 'Clicking on Login')
        driver.find_element(By.XPATH, "//input[@id='login-button']").click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[text()='Products']"))
        )

        print(datetime.now(timezone.utc).strftime(
            "%Y-%m-%d %H:%M:%S  "), "Successfully Logged in as user: {}!".format(user))

    except Exception as err:
        traceback.print_exc()
        raise err


def addtocart():
    try:
        # Waiting for Page Load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[text()='Products']"))
        )

        print(datetime.now(timezone.utc).strftime(
            "%Y-%m-%d %H:%M:%S  "), "Locating all Items")
        itemNames = driver.find_elements(
            By.XPATH, "//*[@class='inventory_item_name']")

        print(datetime.now(timezone.utc).strftime(
            "%Y-%m-%d %H:%M:%S  "), "Clicking on Add to cart for each item")
        for item in itemNames:
            print(datetime.now(timezone.utc).strftime(
                "%Y-%m-%d %H:%M:%S  "), "Clicking on Add to cart for item: {}".format(item.text))
            addToCartElement = driver.find_element(
                By.XPATH, "//*[text()='{}']/ancestor::*[3]//button[text()='Add to cart']".format(item.text))
            addToCartElement.click()
            print(datetime.now(timezone.utc).strftime(
                "%Y-%m-%d %H:%M:%S  "), "Successfully Clicked on Add to cart for item: {}".format(item.text))
        print(datetime.now(timezone.utc).strftime(
            "%Y-%m-%d %H:%M:%S  "), "Successfully Added all Items to Cart!")

    except Exception as err:
        traceback.print_exc()
        raise err


def removefromcart():
    try:
        # Waiting for Page Load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[text()='Products']"))
        )

        print(datetime.now(timezone.utc).strftime(
            "%Y-%m-%d %H:%M:%S  "), "Locating all Items")
        itemNames = driver.find_elements(
            By.XPATH, "//*[@class='inventory_item_name']")

        print(datetime.now(timezone.utc).strftime(
            "%Y-%m-%d %H:%M:%S  "), "Clicking on Remove from cart for each item")

        for item in itemNames:
            print(datetime.now(timezone.utc).strftime(
                "%Y-%m-%d %H:%M:%S  "), "Clicking on Remove from cart for item: {}".format(item.text))
            addToCartElement = driver.find_element(
                By.XPATH, "//*[text()='{}']/ancestor::*[3]//button[text()='Remove']".format(item.text))
            addToCartElement.click()
            print(datetime.now(timezone.utc).strftime(
                "%Y-%m-%d %H:%M:%S  "), "Successfully Clicked on Remove from cart for item: {}".format(item.text))
        print(datetime.now(timezone.utc).strftime(
            "%Y-%m-%d %H:%M:%S  "), "Successfully Removed all Items from Cart!")

    except Exception as err:
        traceback.print_exc()
        raise err

# Main Execution


login('standard_user', 'secret_sauce')
addtocart()
removefromcart()
driver.close()
