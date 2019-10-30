from time import sleep
r = sleep(10)
os.chdir('./moneymaker')

while 1:
    i = []
    for process in psutil.process_iter():
        if process.cmdline[0] == 'python3':
            i.append(process.cmdline())
        else:
            pass
    
    j = [['python3', 'fcm.py', '&'], ['python3', 'cmb.py', '&'], ['python3', 'xyz.py', '&'], ['python3', 'naira.py', '&']]
    for jj in j:
        if jj not in i:
            Popen(jj)
            r
        else:
            r
