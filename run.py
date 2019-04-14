__author__ = "Letícia Bernardo"
__email__ = "leticiaellenbernardo@gmail.com"
__version__ = "0.0.1"
__license__ = "MIT"
__status__ = "Beta"


from tools.selenium_driver import SeleniumDriver

selenium_driver = SeleniumDriver()
driver = selenium_driver.configure_webdriver()

print("Inicializando...")


selenium_driver.close_webdriver(driver)