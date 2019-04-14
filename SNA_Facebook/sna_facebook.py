import time


class FacebookBot:
    def __init__(self, username, password, driver):
        self.username = username
        self.password = password
        self.driver = driver

    def login(self):
        driver = self.driver
        driver.get("https://www.facebook.com/")
        time.sleep(4)

        user_field = driver.find_element_by_id("email")
        user_field.send_keys(self.username)
        time.sleep(1)

        user_field = driver.find_element_by_id("pass")
        user_field.send_keys(self.password)
        time.sleep(1)

        login_button = driver.find_element_by_id("loginbutton")
        login_button.find_elements_by_tag_name('input')[0].click()
        time.sleep(2)