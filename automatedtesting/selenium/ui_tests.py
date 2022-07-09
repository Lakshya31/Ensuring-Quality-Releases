# #!/usr/bin/env python
from asyncio.log import logger
from datetime import datetime, timezone
import logging
import traceback
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as ChromeOptions

logging.basicConfig(filename="selenium_log.txt", level=logging.INFO, format="%(asctime)s %(message)s")

# Start the browser and login with standard_user


def login(user, password):
    try:
        logging.info('Starting the browser...')
        # --uncomment when running in Azure DevOps.
        options = ChromeOptions()
        options.add_argument("--headless")
        global driver
        driver = webdriver.Chrome(options=options)
        # driver = webdriver.Chrome()
        logging.info('Browser started successfully. Navigating to the demo page to login.')
        driver.get('https://www.saucedemo.com/')

        # Waiting for Page Load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@id='user-name']"))
        )

        # Entering Username
        logging.info('Finding Username Input Box')
        username_input_box = driver.find_element(
            By.XPATH, "//input[@id='user-name']")
        logging.info('Entering Username in Input Box')
        username_input_box.send_keys(user)
        logging.info('Entered Username in Input Box!')

        # Entering Password
        logging.info('Finding Password Input Box')
        password_input_box = driver.find_element(
            By.XPATH, "//input[@id='password']")
        logging.info('Entering Password in Input Box')
        password_input_box.send_keys(password)
        logging.info('Entered Password in Input Box!')

        # Click Login
        logging.info('Clicking on Login')
        driver.find_element(By.XPATH, "//input[@id='login-button']").click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[text()='Products']"))
        )

        logging.info("Successfully Logged in as user: {}!".format(user))

    except Exception as err:
        logging.error("The program encountered an error")
        traceback.print_exc()
        raise err


def addtocart():
    try:
        # Waiting for Page Load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[text()='Products']"))
        )

        logging.info("Locating all Items")
        itemNames = driver.find_elements(
            By.XPATH, "//*[@class='inventory_item_name']")

        logging.info("Clicking on Add to cart for each item")
        for item in itemNames:
            logging.info(datetime.now(timezone.utc).strftime(
                "%Y-%m-%d %H:%M:%S  ") + "Clicking on Add to cart for item: {}".format(item.text))
            addToCartElement = driver.find_element(
                By.XPATH, "//*[text()='{}']/ancestor::*[3]//button[text()='Add to cart']".format(item.text))
            addToCartElement.click()
            logging.info(datetime.now(timezone.utc).strftime(
                "%Y-%m-%d %H:%M:%S  ") + "Successfully Clicked on Add to cart for item: {}".format(item.text))
        logging.info("Successfully Added all Items to Cart!")

    except Exception as err:
        logging.error("The program encountered an error")
        traceback.print_exc()
        raise err


def removefromcart():
    try:
        # Waiting for Page Load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[text()='Products']"))
        )

        logging.info("Locating all Items")
        itemNames = driver.find_elements(
            By.XPATH, "//*[@class='inventory_item_name']")

        logging.info("Clicking on Remove from cart for each item")

        for item in itemNames:
            logging.info(datetime.now(timezone.utc).strftime(
                "%Y-%m-%d %H:%M:%S  ") + "Clicking on Remove from cart for item: {}".format(item.text))
            addToCartElement = driver.find_element(
                By.XPATH, "//*[text()='{}']/ancestor::*[3]//button[text()='Remove']".format(item.text))
            addToCartElement.click()
            logging.info(datetime.now(timezone.utc).strftime(
                "%Y-%m-%d %H:%M:%S  ") + "Successfully Clicked on Remove from cart for item: {}".format(item.text))
        logging.info("Successfully Removed all Items from Cart!")

    except Exception as err:
        logging.error("The program encountered an error")
        traceback.print_exc()
        raise err

# Main Execution


login('standard_user', 'secret_sauce')
addtocart()
removefromcart()
driver.close()
logging.info("Execution Complete!")
