from selenium import webdriver
from bs4 import BeautifulSoup
from lxml import etree
import random
import sys
from webdriver_manager.chrome import ChromeDriverManager

from selenium.common.exceptions import TimeoutException, InvalidSessionIdException, SessionNotCreatedException
from selenium.webdriver.chrome.options import Options

sys.path.append("..")
from userAgent import USER_AGENT_LIST


def getSeleniumPage(url,driver):
    try:
        driver.get(url)
    except TimeoutException as Timeout:
        raise
    try:
        page_html = driver.page_source
    except InvalidSessionIdException as InvalidSessionId:
        raise
    page = BeautifulSoup(page_html, 'lxml')
    return page


def createDriverInstance():
    user_agent = random.choice(USER_AGENT_LIST)
    chrome_options = Options()
    chrome_options.add_argument('headless')
    chrome_options.add_argument("window-size=1024,768")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-plugins")
    chrome_options.add_argument("--disable-images")
    chrome_options.add_argument('blink-settings=imagesEnabled=false')
    chrome_options.add_argument(f'user-agent={user_agent}')
    chrome_options.page_load_strategy = 'EAGER'
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)  # Chrome
    driver.set_page_load_timeout(200)
    driver.set_script_timeout(200)
    return driver
