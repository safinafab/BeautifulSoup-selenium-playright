from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,slow_mo=50)
    page= browser.new_page()
    page.goto('https://demo.opencart.com/admin/')
    page.fill('input#input-username','demo',timeout=60000)
    
    page.fill('input#input-password','demo')
    page.click('button[type=submit]')
    time.sleep(2)
    page.is_visible('div.tile-body')
    html=page.inner_html('div#content')
    # print(html)
   
    soup = BeautifulSoup(html,'html.parser')
    total_ordres =soup.find('h2',{'class':'float-end'})
    print(f"total-orders= {total_ordres}")
    # print(soup)
    # print(soup.find_all('h2'))
    
    # page.pause()
    
    