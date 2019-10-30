import selenium.webdriver as webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import time
import requests

profile = webdriver.FirefoxProfile("/home/d3rupt/.mozilla/firefox/6obnlr15.default")
options = Options()
options.headless = True
driver = webdriver.Firefox(firefox_profile=profile, options=options)
   
def cmb():
   # driver.send_keys(Keys.COMMAND + 't')
    url = 'https://cashminingbot.com/mining.php'
    driver.get(url)
    while 1:
        print('cashminingbot running')
        time.sleep(28800)
        driver.refresh()
cmb()
