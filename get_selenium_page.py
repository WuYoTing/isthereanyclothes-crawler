from selenium import webdriver
from bs4 import BeautifulSoup
import random
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException, InvalidSessionIdException
from selenium.webdriver.chrome.options import Options
from user_agent_list.userAgent import user_agent_list


def get_selenium_page(url, driver):
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


def create_driver_instance():
    user_agent = random.choice(user_agent_list)
    chrome_options = Options()
    chrome_options.add_argument('headless')
    chrome_options.add_argument("window-size=1024,768")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-plugins")
    chrome_options.add_argument("--disable-images")
    chrome_options.add_argument('blink-settings=imagesEnabled=false')
    chrome_options.add_argument(f'user-agent={user_agent}')
    chrome_options.add_argument('log-level=3')
    chrome_options.page_load_strategy = 'EAGER'
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)  # Chrome
    driver.set_page_load_timeout(5000)
    driver.set_script_timeout(5000)
    return driver
