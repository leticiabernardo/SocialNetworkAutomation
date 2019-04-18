from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
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

    def like_photo_by_hashtag(self, hashtag):
        driver = self.driver
        driver.get('https://www.instagram.com/explore/tags/' + hashtag + '/')
        time.sleep(2)

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

        element_links = driver.find_elements_by_tag_name('a')
        links_pic_href = [elem.get_attribute('href') for elem in element_links]

        for pic_href in links_pic_href:
            driver.get(pic_href)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            try:
                driver.find_element_by_xpath("//button/span[@aria-label='Curtir']").click()
                time.sleep(4)
            except Exception as e:
                print("Error:", e)
                time.sleep(2)

    def follow_by(self, copy_followers_from):
        driver = self.driver

        driver.get('https://www.instagram.com/' + copy_followers_from + '/')
        time.sleep(2)

        try:
            login_button = driver.find_element_by_xpath("//a[@href='/" + copy_followers_from + "/followers/']")
            login_button.click()
            time.sleep(2)

            driver.execute_script("document.getElementsByClassName('isgrP')[0].scroll(0,900)")
            driver.execute_script("document.getElementsByClassName('isgrP')[0].scroll(0,900)")
            time.sleep(2)

            users_follow = driver.find_elements_by_css_selector(".isgrP li > div")

            for user in users_follow:
                button_action = user.find_element_by_css_selector("button")
                # username_following = user.find_element_by_css_selector("div > div a").get_attribute("href")

                if button_action.text == 'Seguir':
                    button_action.click()
                    time.sleep(2)

        except NoSuchElementException:
            return 0


