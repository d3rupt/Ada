import pyowm
import time
from datetime import datetime

now = datetime.now()
owm = pyowm.OWM('fc1e626cf9767a060d5f305178089700')
wpg = owm.weather_at_place('Winnipeg, CA')
weather = wpg.get_weather()
sunset = weather.get_sunset_time(timeformat='iso')
while 1:
    sunset = weather.get_sunset_time(timeformat='iso')
    print(sunset)
    sunset = sunset.split(' ')
    sunset1 = []
    for s in sunset:
        if ':' in s:
            sunset1.append(s)
        else:
            pass
    
    print(sunset1)
    sunset = str(sunset1[0])
    sunset = sunset.split(':')
    print(sunset)
    s = int(sunset[0])
    s = str(s - 6)
    print(s)
    sunset.insert(0, s)
    c = ':'
    del sunset[2:4]
    sunset = c.join(sunset)
    print(sunset)
    
    if now.strftime('%H:%M') == sunset:
        requests.get(lamp + '/sunset')
    else:
        for i in range(10, 0, -1):
            print('resuming in {} seconds'.format(str(i)))
            time.sleep(1)