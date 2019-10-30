import threading, time, sys
from datetime import datetime
import selenium.webdriver as webdriver
from selenium.webdriver.firefox.options import Options

now = datetime.now()
profile = webdriver.FirefoxProfile("/home/d3rupt/.mozilla/firefox/6obnlr15.default")
options = Options()
options.headless = False
driver = webdriver.Firefox(firefox_profile=profile, options=options)

class money:
    def fcm(self):
    
        #options.add_argument("user-data-dir=/home/d3rupt/.mozilla/firefox/6obnlr15.default")
        url = "https://fastcashmining.com/mining.php"
        while 1:
            driver.get(url)
            print('fastcashmining running.')
            time.sleep(1440)
            driver.close()
    
    def cmb(self):
        #options = Options()
        #options.headless = False
        #options.add_argument("user-data-dir=/home/d3rupt/.mozilla/firefox/6obnlr15.default")
        url = 'https://cashminingbot.com/mining.php'
        while 1:
            driver.get(url)
            print('cashminingbot running')
            time.sleep(1440)
            driver.close()
    
    def xyz(self):
    #    options = Options()
    #   options.headless = False
    #  options.add_argument("user-data-dir=/home/d3rupt/.mozilla/firefox/6obnlr15.default")
        url = 'https://moneymining.xyz/mining.php'
        while 1:
            driver.get(url)
            print('moneymining running')
            time.sleep(1440)
            driver.close()
        
    def naira(self):
    #   options = Options()
    #  options.headless = False
    # options.add_argument("user-data-dir=/home/d3rupt/.mozilla/firefox/6obnlr15.default")
        url = 'https://minenaira.com/mining.php'
        while 1:
            driver.get(url)
            print('minenaira running')
            time.sleep(1440)
            driver.close()
    
fcm = threading.Thread(target = money().fcm()).start()
cmb = threading.Thread(target = money().cmb()).start()
xyz = threading.Thread(target = money().xyz()).start()
naira = threading.Thread(target = money().naira()).start()
cmb