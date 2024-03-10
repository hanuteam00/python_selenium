from selenium import webdriver
import time

# driver = webdriver.Chrome()
driver = webdriver.Firefox()
driver.set_window_size(1200, 800)  # Set your desired window size

# Open a website
driver.get("https://www.dantri.com.vn")

driver.get_screenshot_as_file("screenshot2.png")

time.sleep(5)
print('End testing')
# print(driver.get_log("browser"))

driver.quit()



"""
from selenium import webdriver

# Specify the path to the ChromeDriver executable
chrome_driver_path = "./python_selenium/chromedriver-mac-x64/chromedriver"

# Set up Chrome options
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")  # Optional: Run Chrome in headless mode
chrome_options.add_argument(f"chromedriver={chrome_driver_path}")

# Initialize the Chrome driver with Chrome options
driver = webdriver.Chrome(options=chrome_options)

# Open a website
driver.get("https://www.example.com")

# Perform actions (e.g., find elements, interact with them)
# ...

# Close the browser window
# driver.quit()
"""