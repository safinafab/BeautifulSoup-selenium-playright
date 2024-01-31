from selenium import webdriver
#our brower  gets closed as soon as it is opened so to keep it open after the program gets over

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
# driver.get
driver = webdriver.Chrome(executable_path= "Downloads/chromedriver_win32/chromedriver.exe")
# webdriver.Chrome(executable_path=Downloads\chromedriver_win32_2.0\chromedriver.exe')
driver.get("https://www.amazon.com/")
driver.quit()
