# https://www.browserstack.com/guide/install-selenium-python-on-macos
from selenium import webdriver 
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC;

import json
import warnings
import time

"""
Way 2 for geckodriver
gecko_driver_path = "./python_selenium/geckodriver"
# Set up Firefox options
firefox_options = webdriver.FirefoxOptions()
firefox_options.headless = False  # Optional: Run Firefox in headless mode
firefox_options.binary_location = "/path/to/firefox"  # Specify the path to Firefox binary if not in PATH
firefox_options.add_argument(f"webdriver.gecko.driver={gecko_driver_path}")
# Initialize the Firefox driver with executable path and options
driver = webdriver.Firefox(options=firefox_options)
"""



warnings.filterwarnings("ignore")

with open('browserstack_config_v2.json') as json_file:
    config_data = json.load(json_file)

for curr_config in config_data['browsers']:
    curr_browser = curr_config['browser']
    curr_search_term = curr_config['search_term']

    if(curr_browser=='chrome'): 
        driver = webdriver.Chrome()
        """
        this does not work
        driver = webdriver.Chrome(executable_path='./python_selenium/webdrivers/chromedriver')
        """

    elif(curr_browser=='firefox'):
        # driver = webdriver.Firefox()
        # Way 2 for geckodriver
        gecko_driver_path = "./python_selenium/webdrivers/geckodriver"
        # Set up Firefox options
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.headless = False  # Optional: Run Firefox in headless mode
        firefox_options.binary_location = "/path/to/firefox"  # Specify the path to Firefox binary if not in PATH
        firefox_options.add_argument(f"webdriver.gecko.driver={gecko_driver_path}")
        # Initialize the Firefox driver with executable path and options
        driver = webdriver.Firefox(options=firefox_options)

        
    try: 
        #remember f
        print(f'1. Opening Website for {curr_browser}') 
        url = 'http://www.google.com'
        driver.get(url)

        # print("page_source 1: " +driver.page_source)
        # main = driver.find_element_by_id("main")

        print('2. Performing test')
        # main = driver.find_element(By.ID,"snbc")
        # print("main 1: " +main.text)
        try:
            searchElement = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, 'q'))
            )
        except:
            print("Element is not visible")
            driver.quit()
        inputElement = driver.find_element(By.NAME, 'q')
        # findElement = driver.find_element(By.XPATH, "(//input[@name='btnK'])[2]")
        time.sleep(3)
        inputElement.send_keys(curr_search_term)
        time.sleep(3)
        # findElement.click()
        inputElement.submit()
        time.sleep(5)
        
        print('3a. Test is Successful')
        
    except Exception as e:
        print('3b. Test is Unsuccessful')
        # Close the browser window
    
    finally:
        # Close the browser window in the finally block to ensure it's closed even if an exception occurs
        driver.quit()