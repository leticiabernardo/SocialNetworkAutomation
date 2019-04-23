__author__ = "Letícia Bernardo"
__email__ = "leticiaellenbernardo@gmail.com"
__version__ = "0.0.1"
__license__ = "MIT"
__status__ = "Beta"

from tools.selenium_driver import SeleniumDriver
from SNA_Facebook.sna_facebook import FacebookBot
#from SNA_Instagram.sna_instagram import InstagramBot
import tools.helpers as helper
import config

selenium_driver = SeleniumDriver()
driver = selenium_driver.configure_webdriver(config.HIDE_BROWSER)

print("Inicializando...")

# ---------------
# FACEBOOK BOT
faceBot = FacebookBot(config.FACEBOOK_USERNAME, helper.clean_password(config.FACEBOOK_PASSWORD), driver)
faceBot.login()
#faceBot.say_happy_birthday()
faceBot.like_posts()


# ---------------
# INSTAGRAM BOT
#instaBot = InstagramBot(config.INSTA_USERNAME, helper.clean_password(config.INSTA_PASSWORD), driver)
#instaBot.login()

# for tag in helper.string_to_array(config.INSTA_TAGS_FOLLOW):
#     instaBot.like_photo_by_hashtag(tag)

# for user in helper.string_to_array(config.INSTA_COPY_FOLLOWERS_FROM):
#     instaBot.follow_from(user)

#instaBot.unfollow(helper.string_to_array(config.INSTA_UNFOLLOW_DISABLED))


selenium_driver.close_webdriver(driver)
