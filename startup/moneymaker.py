import time
import psutil
from subprocess import Popen
import os

r = time.sleep(10)
os.chdir('./moneymaker')

while 1:
    i = []
    for process in psutil.process_iter():
        p = process.cmdline()
        i.append(process.cmdline())

    
    j = [['python3', 'fcm.py', '&'], ['python3', 'cmb.py', '&'], ['python3', 'xyz.py', '&'], ['python3', 'naira.py', '&']]
    for jj in j:
        if jj not in i:
            Popen(jj)
            r
        else:
            r
