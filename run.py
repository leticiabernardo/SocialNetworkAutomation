__author__ = "Letícia Bernardo"
__email__ = "leticiaellenbernardo@gmail.com"
__version__ = "0.0.1"
__license__ = "MIT"
__status__ = "Beta"

from tools.selenium_driver import SeleniumDriver
from SNA_Facebook.sna_facebook import FacebookBot
import tools.helpers as helper
import config

selenium_driver = SeleniumDriver()
driver = selenium_driver.configure_webdriver()

print("Inicializando...")

facebookTest = FacebookBot(config.FACEBOOK_USERNAME, helper.clean_password(config.FACEBOOK_PASSWORD), driver)
facebookTest.login()

selenium_driver.close_webdriver(driver)
