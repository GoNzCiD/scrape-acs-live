# For Windows
# download chromedriver
# https://www.scrapingbee.com/blog/selenium-python/

# For linux
# sudo apt install chromium-chromedriver
# pip install selenium
import logging
import sys
import urllib

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options

from common import WINDOWS_CHROME_DRIVER_PATH, SERVER_URL, MULTISERVER_ID, USER, PASSWORD

LIVE_URL_PATH = "/live-timing"


class AssettoServerBrowser:
    def __init__(self):
        url_parse = urllib.parse.urlparse(SERVER_URL)
        self.live_url = urllib.parse.urlunparse((url_parse.scheme, url_parse.hostname, LIVE_URL_PATH, None,
                                                 "server={}".format(MULTISERVER_ID), None))
        self.browser = self._create_headless_chrome_browser()

    def __enter__(self):
        self.browser.get(self.live_url)
        try:
            login_form = self.browser.find_element_by_xpath("//form[@action='/login']")
            login_form.find_element_by_id("Username").send_keys(USER)
            login_form.find_element_by_id("Password").send_keys(PASSWORD)
            login_form.submit()
            self.browser.get(self.live_url)
        except NoSuchElementException as e:
            logging.error("No login form found! - {}".format(e))
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.browser.quit()

    def get_living_time(self):
        live_table = ""
        live_table_disconnected = ""
        try:
            for table in self.browser.find_elements_by_tag_name("table"):
                if table.get_attribute("id") == "live-table":
                    live_table = table.get_attribute('outerHTML')
                elif table.get_attribute("id") == "live-table-disconnected":
                    live_table_disconnected = table.get_attribute('outerHTML')
        except NoSuchElementException as e:
            logging.error("No live result tables found! - {}".format(e))

        return live_table, live_table_disconnected

    @staticmethod
    def _create_headless_firefox_browser():
        # Needed to install geckodriver: https://stackoverflow.com/a/40208762
        options = webdriver.FirefoxOptions()
        options.add_argument('--headless')
        return webdriver.Firefox(options=options)

    @staticmethod
    def _create_headless_chrome_browser():
        # options = webdriver.ChromeOptions()
        # options.add_argument('headless')
        options = Options()
        options.headless = True
        options.add_argument("--window-size=1920,1200")
        if sys.platform == 'win32':
            return webdriver.Chrome(executable_path=WINDOWS_CHROME_DRIVER_PATH, options=options)
        return webdriver.Chrome(options=options)
