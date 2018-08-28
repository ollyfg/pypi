from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#set a headless browser
options = webdriver.ChromeOptions()
# options.add_argument('headless')
options.add_argument("--window-size=1920x1080")
options.add_argument("--kiosk")
options.add_argument("--disable-infobars");
browser = webdriver.Chrome(chrome_options=options)

browser.get("https://www.google.com")
print browser.title

inputElement = browser.find_element_by_name("q")
inputElement.send_keys("cheese!")
inputElement.submit()

try:
    WebDriverWait(browser, 10).until(EC.title_contains("cheese!"))
    print browser.title
finally:
    browser.quit()
