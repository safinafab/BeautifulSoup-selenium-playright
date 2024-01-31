from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# driver = webdriver.Chrome(service=webdriver.chrome.service.Service(executable_path="C:/Users/Safina/Downloads/chromedriver_win32"))
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get('https://www.programsbuzz.com')