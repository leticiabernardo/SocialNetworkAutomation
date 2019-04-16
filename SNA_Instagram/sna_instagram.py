from selenium.webdriver.common.keys import Keys
import time


class InstagramBot:
    def __init__(self, username, password, driver):
        self.username = username
        self.password = password
        self.driver = driver

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)

        user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
        user_name_elem.clear()
        user_name_elem.send_keys(self.username)

        user_password_elem = driver.find_element_by_xpath("//input[@name='password']")
        user_password_elem.clear()
        user_password_elem.send_keys(self.password)
        user_password_elem.send_keys(Keys.RETURN)
        time.sleep(2)
