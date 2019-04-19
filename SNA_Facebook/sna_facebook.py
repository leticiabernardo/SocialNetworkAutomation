from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
from tools.make_txt import MakeTxt
import tools.helpers as helper


class FacebookBot:
    def __init__(self, username, password, driver):
        self.username = username
        self.password = password
        self.driver = driver
        self.make_txt = MakeTxt()

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

    def say_happy_birthday(self):
        driver = self.driver
        driver.get("https://www.facebook.com/events/birthdays/")
        time.sleep(4)
        self.clean_page(driver)

        for element in self.driver.find_elements_by_css_selector('li._tzm'):
            person_name_obj = element.find_element_by_tag_name("a")

            try:
                text_area_field = element.find_element_by_tag_name("textarea")
                happy_birthday_text = helper.happy_birthday_message(self.make_txt)
                text_area_field.send_keys(happy_birthday_text)
                person_name = person_name_obj.text

                time.sleep(1)
                text_area_field.send_keys(Keys.RETURN)
                time.sleep(1)

                data = "\n" + person_name + " | " + happy_birthday_text
                self.make_txt.save_data("activities/historic_happy_birthday", data)

            except NoSuchElementException:
                pass

    @staticmethod
    def clean_page(driver):
        try:
            driver.find_elements_by_class_name("_3ixn")[0].click()
        except IndexError:
            pass

        try:
            driver.find_elements_by_class_name("AdBox")[0].click()
        except IndexError:
            pass

        try:
            driver.find_elements_by_class_name("Ad")[0].click()
        except IndexError:
            pass

        try:
            driver.find_elements_by_class_name("advert")[0].click()
        except IndexError:
            pass
