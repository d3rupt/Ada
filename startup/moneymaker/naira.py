import selenium.webdriver as webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import time

profile = webdriver.FirefoxProfile("/home/d3rupt/.mozilla/firefox/6obnlr15.default")
options = Options()
options.headless = False
driver = webdriver.Firefox(firefox_profile=profile, options=options)

def naira():
  #  driver.send_keys(Keys.COMMAND + 't')
    url = 'https://minenaira.com/mining.php'
    driver.get(url)
    while 1:
        print('minenaira running')
        time.sleep(28800)
       # driver.refresh()
naira()