__author__ = "Letícia Bernardo"
__email__ = "leticiaellenbernardo@gmail.com"
__version__ = "0.0.1"
__license__ = "MIT"
__status__ = "Beta"

from tools.selenium_driver import SeleniumDriver
# from SNA_Facebook.sna_facebook import FacebookBot
from SNA_Instagram.sna_instagram import InstagramBot
import tools.helpers as helper
import config

selenium_driver = SeleniumDriver()
driver = selenium_driver.configure_webdriver()

print("Inicializando...")

#faceBot = FacebookBot(config.FACEBOOK_USERNAME, helper.clean_password(config.FACEBOOK_PASSWORD), driver)
#faceBot.login()
#faceBot.say_happy_birthday()

instaBot = InstagramBot(config.INSTA_USERNAME, helper.clean_password(config.INSTA_PASSWORD), driver)
instaBot.login()
[instaBot.like_photo_by_hashtag(tag) for tag in helper.string_to_array(config.INSTA_TAGS_FOLLOW)]

selenium_driver.close_webdriver(driver)

