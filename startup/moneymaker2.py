import selenium.webdriver as webdriver
from selenium.webdriver.firefox.options import Options
import time, threading

profile = webdriver.FirefoxProfile("/home/d3rupt/.mozilla/firefox/6obnlr15.default")
options = Options()
options.headless = False
driver = webdriver.Firefox(firefox_profile=profile, options=options)

class moneymake:
    def __init__(self, url):
        self.url = url
        
    def moneymaker(self):
        driver.get(self.url)
        while 1:
            time.sleep(28800)
            driver.refresh()
            
cmb = moneymake('https://cashminingbot.com/mining.php')
fcm = moneymake("https://fastcashmining.com/mining.php")
xyz = moneymake('https://moneymining.xyz/mining.php')

cmb = threading.Thread(target = cmb().moneymaker).start()
fcm = threading.Thread(target = fcm().moneymaker).start()
xyz = threading.Thread(target = xyz().moneymaker).start()
