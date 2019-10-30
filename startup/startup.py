import time, psutil, os
from subprocess import Popen
r = time.sleep(5)

while 1:
    p = []
    os.chdir('/home/d3rupt/Projects/Ada/startup')
    r
    r
    for process in psutil.process_iter():
        if 'python3' in process:
            p.append(process.cmdline())
        else:
            pass
                
    #if ['python3', 'security.py', '&'] not in p:
        #Popen(['python3', 'security.py', '&'])
        #print('SECURITY MEASURES INITIALIZED\n')
    
    prcs = [['python3', 'workout.py', '&'], ['python3', 'moneymaker.py', '&']]
    for pr in prcs:
        if pr not in p:
            Pr = pr[1].upper()
            Popen(pr)
            print('|---' + Pr[0:-3] + ' INITIALIZED---|\n--\n')
        else:
            pass
            