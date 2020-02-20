

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time


def start_chrome(headless=False):

    chrome_options = Options()
    chrome_options.add_argument(
          f'--user-agent="Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.10; rv:62.0) Gecko/20100101 Firefox/62.0"')
    chrome_options.add_argument('--blink-settings=imagesEnabled=false')
    if headless:
        chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')

    driver = webdriver.Chrome(options=chrome_options)
    driver.delete_all_cookies()
    return driver


chrome_driver = start_chrome(headless=True)

# input query
query = 'China Eastern Airlines'

url = 'https://www.allacronyms.com/' + '_'.join(query.lower().split(' ')) + '/abbreviated'

try:
    chrome_driver.get(url)
    WebDriverWait(chrome_driver, 100, 0.5).until(
        expected_conditions.presence_of_element_located((By.XPATH, "//div")))
except Exception as e:
    print(e)

time.sleep(0.5)

element = None
try:
    element = chrome_driver.find_element_by_class_name('terms_items')
except NoSuchElementException:
    pass
abbr_set = element.text.split('\n')[::2] if element else None

# output
print(abbr_set)
