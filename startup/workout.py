from imapclient import IMAPClient
import random
from datetime import datetime
import time
import smtplib, ssl
from email.mime.text import MIMEText

def email(email, content):
    port = 465  # For SSL
# Create a secure SSL context
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("thisisada69@gmail.com", "Coulson1")
        server.sendmail("thisisada69@gmail.com", email, content)
        server.close()
        
imap_host = 'imap.gmail.com'
imap_user = 'thisisada69@gmail.com'
imap_pass = 'Coulson1'
n = 'thdnkns@gmail.com'

#lists of workouts embedded in links
wk = [['<a href=\'https://www.jetts.com.au/jetts-life/workouts/7-stretches-you-should-be-doing-after-every-workosut\'>10 mins stretch</a>',
'<a href=\https://blog.johnsonfitness.com/blog/high-intensity-interval-training-hiit-treadmill/\'>15 min run</a>',
'<a href=\'\https://stronglifts.com/overhead-press/\'>Overhead barbell press, 4x8</a>',
'<a href=\'https://stronglifts.com/overhead-press/\'>Barbell pull-up\, 4x8</a>',
'<a href=\'https://www.onnit.com/academy/1-exercise-that-fixes-99-problems/\'>Kettlebell swing\, 4x8</a>',
'<a href=\'https://www.mmarevolution.com/heavy-bag-workouts/\'>Punching bag\, 5x30sec</a>',
'10k steps'],

['<a href=\'https://www.jetts.com.au/jetts-life/workouts/7-stretches-you-should-be-doing-after-every-workout\'>10 mins stretch</a>',
'<a href=\'https://www.self.com/story/4-ways-to-turn-the-stationary-bike-into-a-fat-burning-machine\'>15 min bike\'</a>',
'<a href=\'\'>Rowing, 4x8</a>',
'<a href=\'https://kettlebellsworkouts.com/teaching-points-for-the-kettlebell-overhead-press/\'>Overhead kettlebell press\, 4x8</a>',
'<a href=\'https://kettlebellsworkouts.com/kettlebell-deadlift/\'>Kettlebell deadlift\, 4x8,</a>',
'<a href=\'https://www.expertboxing.com/boxing-strategy/fight-tips/basic-boxing-footwork-strategy\'>Punching bag, 5x30sec\</a>',
'10k steps']]


while 1:
    e = ''
    dailyworkout = []
    dailyworkout = random.choice(['push-ups x100', 'sit-ups x100', 'burpees x50'])
    now = datetime.now()
    hour = now.strftime('%H')
    srvr = IMAPClient(imap_host, use_uid=True)
    srvr.login(imap_user, imap_pass)
    srvr.select_folder('INBOX', readonly=False)
    hh = srvr.search(['FROM',  'thdnkns@gmail.com'])
    #print(hh)
    for msgid, data in srvr.fetch(hh, ['ENVELOPE']).items():
        envelope = data[b'ENVELOPE']
        e = envelope.subject.decode()
    if e == 'Gym':
        with open('workout.txt', 'r') as whichone:
            print('so far')
            if '0' in whichone.read():
                print('chose workout')
                items = ["\n    <li>{}</li>".format(s) for s in wk[0]]
                items = "".join(items)
                list1 = '''\
                <html>
                <head>
                </head>
                <ul style="font-family: trebuchet;">
                <h2>Hi! Here's your workout for today:</h2>
                <ul style="border: 1px solid black; padding: 40px;">
                {}
                </ul>
                </body>
                </html>
                '''.format(items)
                print('formatted email')
                list1 = MIMEText(list1, 'html')
                email(email=n, content=list1.as_string())
                print('email sent')
                srvr.delete_messages(hh) 
                print('deleted')
                whichone.close()
                whichone = open('workout.txt', 'w')  
                whichone.write('1')
                whichone.close()
                srvr.logout()
                time.sleep(10)
            else:
                print('chose workout')
                items = ["\n    <li>{}</li>".format(s) for s in wk[1]]
                items = "".join(items)
                list1 = '''\
                <html>
                <head>
                </head>
                <ul style="font-family: trebuchet;">
                <h2>Hi! Here's your workout for today:</h2>
                <ul style="border: 1px solid black; padding: 40px;">
                {}
                </ul>
                </body>
                </html>
                '''.format(items)
                print('formatted email')
                list1 = MIMEText(list1, 'html')
                email(email=n, content=list1.as_string())
                print('email sent')
                srvr.delete_messages(hh) 
                print('deleted')
                whichone.close()
                whichone = open('workout.txt', 'w')  
                whichone.write('0')
                whichone.close()
                srvr.logout()
                time.sleep(10)

    elif e == 'No gym':
        email(email='thdnkns@gmail.com', content='Hi!. Here is your off-day workout:\n' + dailyworkout)
        srvr.delete_messages(hh)
        srvr.logout()
        time.sleep(10)
        
    else:
        srvr.logout()
        time.sleep(10)
