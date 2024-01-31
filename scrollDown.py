from playwright.sync_api import sync_playwright

def handle_ajax(response):
    try:
        if 'https://k-eu1.az.contentsquare.net/v2/recording?' in response.url:
            print({'url':response.url,'body':response.json()})
    except:
        print("no data")


with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()
    page.on('response',lambda response:handle_ajax(response))
    page.goto("https://www.versace.com/in/en/men/shoes/?start=0&sz=100")
    page.wait_for_timeout(3000)
    cli=page.wait_for_selector('//*[@id="onetrust-accept-btn-handler"]').click()
    for i in range(1,3):
        scroll=page.mouse.wheel(0,1500)
        page.wait_for_timeout(6000)
    