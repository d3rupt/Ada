import selenium.webdriver as webdriver
from selenium.webdriver.firefox.options import Options
import time

profile = webdriver.FirefoxProfile("/home/d3rupt/.mozilla/firefox/6obnlr15.default")
options = Options()
options.headless = False
driver = webdriver.Firefox(firefox_profile=profile, options=options)

def fcm():
    url = "https://fastcashmining.com/mining.php"
    while 1:
        driver.get(url)
        print('fastcashmining running.')
        time.sleep(28800)
        driver.close()
fcm()