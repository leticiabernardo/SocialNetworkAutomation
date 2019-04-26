from selenium import webdriver
import platform


class SeleniumDriver:

    @staticmethod
    def configure_webdriver(browser='chrome', hide_browser=1):
        driver = None
        if platform.system() == 'Windows':
            if browser == 'chrome':
                # ChromeDriver 2.41
                # https://chromedriver.storage.googleapis.com/index.html?path=2.41/
                options = webdriver.ChromeOptions()
                if hide_browser == 1:
                    options.add_argument("--headless")

                options.add_argument('--ignore-certificate-errors')
                options.add_argument('--ignore-ssl-errors')
                options.add_argument("--disable-notifications")
                driver = webdriver.Chrome(chrome_options=options, executable_path=r"setup/windows/chromedriver.exe")
            elif browser == 'firefox':
                driver = webdriver.Firefox(executable_path=r'setup/linux/geckodriver.exe')
        else:
            if browser == 'chrome':
                options = webdriver.ChromeOptions()
                if hide_browser == 1:
                    options.add_argument("--headless")

                options.add_argument('--ignore-certificate-errors')
                options.add_argument('--ignore-ssl-errors')
                options.add_argument("--disable-notifications")
                driver = webdriver.Chrome(chrome_options=options, executable_path=r"setup/linux/chromedriver")

            elif browser == 'firefox':
                options = webdriver.FirefoxOptions()
                if hide_browser == 1:
                    options.add_argument('-headless')

                driver = webdriver.Firefox(executable_path="./setup/linux/geckodriver", firefox_options=options)

        driver.maximize_window()
        return driver

    @staticmethod
    def close_webdriver(driver):
        driver.close()
        driver.quit()
