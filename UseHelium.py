from helium import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"
chromedriver_path = 'chromedriver.exe'
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()), options=options)
driver.maximize_window()
driver.get(url=url)
browser = start_chrome(url=url,headless=True)
# html = browser.page_source
# print(html)
