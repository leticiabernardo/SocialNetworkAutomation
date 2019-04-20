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
        time.sleep(2)

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

        for element in driver.find_elements_by_css_selector('li._tzm'):
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

    def like_posts(self):
        driver = self.driver

        if driver.current_url != "https://www.facebook.com/":
            driver.get("https://www.facebook.com/")
            time.sleep(4)

        self.clean_page(driver)

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        for i in range(1, 3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)

        posts2 = driver.find_element_by_css_selector("[role='feed']")
        feed_history = posts2.find_elements_by_css_selector("[data-testid='fbfeed_story']")

        try:
            for post in feed_history:
                like = post.find_element_by_css_selector("[data-testid='UFI2ReactionLink']")

                if like.get_attribute("aria-pressed") == "false":
                    try:
                        z = "arguments[0].setAttribute('style', 'position:relative;z-index:99999')"
                        driver.execute_script(z, like)
                        time.sleep(1)
                        x = str(int(like.location['x']))
                        y = str(int(like.location['y']))
                        driver.execute_script("window.scrollTo(" + x + "," + y + ")")
                        time.sleep(1)

                        try:
                            like.click()
                        except Exception as err2:
                            time.sleep(3)
                            try:
                                driver.find_elements_by_class_name('layerCancel')[0].click()
                            except NoSuchElementException:
                                pass

                            print("ERR 2:", err2)

                    except Exception as err:
                        time.sleep(3)
                        try:
                            driver.find_elements_by_class_name('layerCancel')[0].click()
                        except NoSuchElementException:
                            pass
                        print(err)

        except NoSuchElementException:
            print("Não há postagens")
            pass

    @staticmethod
    def clean_page(driver):
        try:
            driver.find_elements_by_class_name("_3ixn")[0].click()
        except IndexError:
            pass
