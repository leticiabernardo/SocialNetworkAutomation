from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import platform


class SeleniumDriver:
    #def __init__(self):
        #self.driver = self.configure_webdriver()

    @staticmethod
    def configure_webdriver():
        if platform.system() == 'Windows':
            # ChromeDriver 2.41
            # https://chromedriver.storage.googleapis.com/index.html?path=2.41/
            options = webdriver.ChromeOptions()
            options.add_argument('--ignore-certificate-errors')
            options.add_argument('--ignore-ssl-errors')
            driver = webdriver.Chrome(chrome_options=options, executable_path=r"setup/windows/chromedriver.exe")
        else:
            # Geckodriver
            # driver = webdriver.Firefox()

            options = webdriver.ChromeOptions()
            options.add_argument('--ignore-certificate-errors')
            options.add_argument('--ignore-ssl-errors')
            driver = webdriver.Chrome(chrome_options=options, executable_path=r"setup/linux/chromedriver")

            # from selenium import webdriver
            # from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
            #
            # binary = FirefoxBinary('path/to/installed firefox binary')
            # browser = webdriver.Firefox(firefox_binary=binary)

        driver.maximize_window()
        return driver

    @staticmethod
    def close_webdriver(driver):
        driver.close()
        driver.quit()

    @staticmethod
    def check_browser():
        if platform.system() == 'Windows':
            print("Windows")
        else:
            print("linux")
