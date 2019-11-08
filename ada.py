import speech_recognition as sr
import time
import requests
import os
from gtts import gTTS
import smtplib, ssl
import random
import wolframalpha
import selenium.webdriver as webdriver
from selenium.webdriver.firefox.options import Options
from playsound import playsound
from datetime import datetime
from pyowm import OWM
from pyowm.caches.lrucache import LRUCache
from email.mime.text import MIMEText
#import psutil
import pychromecast
from tqdm import tqdm

#==============================================================================#
#----------------------Database------------------------------------------------#
#==============================================================================#

emails = {
'Otis':'monkay03@hotmail.com',
'me': 'thdnkns@gmail.com'
}

menu = {
	
'Roast Chicken':
'Chicken\n\n',

'Burritos':
['Cheese\n',
'Wraps\n',
'Refried beans\n',
'Mexican rice\n',
'Canned corn\n',
'Chicken\n',
'Taco seasoning\n',
'no side\n'],

'Enchiladas':
['Cheese\n',
'Chicken\n',
'Wraps\n',
'Tomato sauce\n',
'Chicken stock\n',
'Taco seasoning\n',
'summer\n'],

'Sheperds pie':
['Potatoes\n',
'Ground beef\n',
'Creamed corn\n',
'Veggies\n',
'Brown gravy\n',
'Milk\n',
'no side\n'],

'Meatloaf':
['Eggs\n',
'Breadcrumbs or ShakenBake mix\n',
'Ground beef\n',
'BBQ sauce\n'],

'Stir fry':
['Veggies\n',
'Rice\n',
'Eggs\n',
'Soy sauce\n',
'Hot sauce\n',
'Meat\n',
'no side\n'],

'Quesadillas':
['Wraps\n',
'Cheese\n',
'Meat\n',
'Taco seasoning\n',
'summer\n'],

'Mac n cheese':
['Pasta\n',
'Cheese\n',
'Milk\n',
'Flour\n',
'Additions (Bacon, meat, veggies, etc)\n',
'no side\n'],


'Smokies':
['Smokies\n',
'Buns\n',
'summer\n'],

'Burgers':
['Buns\n',
'Ground beef\n',
'Tomatoes\n',
'Lettuce\n',
'Eggs\n',
'Garlic powder\n',
'Milk\n',
'Crackers\n',
'summer\n'],

'Peanut chicken stir fry':
['Peanuts\n',
'Peanut butter\n',
'Sriracha\n',
'Lime\n',
'Rice\n',
'Vegetable\n',
'Garlic\n',
'no side\n'],

'Hot dogs':
['Hot dog buns\n',
'Hot dogs\n',
'summer\n'],

'Pork with apple sauce':
['Pork\n',
'Apple juice or apples\n',
'Thyme\n'
'Butter\n',
'Stock\n'],
	
'Taco salad':
['Lettuce\n',
'Tomato\n',
'Cheese\n',
'Catalina\n',
'Ground beef\n',
'Tostitos\n',
'Avocado\n'
'no side\n'],

'Thai curry':
['Vegetables\n',
'Curry paste\n',
'Stock\n',
'Chicken, pork, chickpeas or cauliflower\n',
'Coconut milk\n',
'Rice\n',
'Lime\n'
'no side\n'],
	
'ShakeNbake':
['Chicken or pork\n',
'ShaneNbake mix\n'],

'Spaghetti':
['Ground beef\n',
'Tomato sauce\n',
'Mushrooms\n',
'Pasta\n',
'Onions']

}

#==============================================================================#
#----------------------------------Variables-----------------------------------#
#==============================================================================#
shoppingList = 'shoppingList.txt'
gotIt = './audio/sys/light.ogg'
fail = '/audio/sys/botwfail.flac'
yip = ['yes', 'yeah', 'sounds good', 'ok', 'sure']
nupe = ['no', 'nope', 'noop', 'nah', 'no way']
#==============================================================================#		
#--------------------------Eyes and ears---------------------------------------#
#==============================================================================#

def speak(audioString):
	print(audioString)
	tts = gTTS(text=audioString, lang='en-GB')
	tts.save("audio.mp3")
	os.system("mpg321 audio.mp3")
 
def recordAudio():
# Record Audio
	r = sr.Recognizer()
	with sr.Microphone() as source:
		audio = r.listen(source)
 
# Speech recognition using Google Speech Recognition
	data = ""
	try:
# Uses the default API key
# To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
		data = r.recognize_google(audio)
		print("You said: " + data)
	except sr.UnknownValueError as f:
		print("Ada could not understand audio")
		
	except sr.RequestError as e:
		print("Could not request results from Google Speech Recognition service; {0}".format(e))
	return data

#==============================================================================#
#----------------------------------Her brains----------------------------------#
#==============================================================================#

def play(sound): #catch all play sound function
	os.system('mpg321 gain 100 {}'.format(sound))
	
def deeper():
	data  = recordAudio()
	while 1:
		data
		
def forDinner():	 #meal planning
	tryAgain = True
	while tryAgain == True:
		tonight = menu.keys()
		tonight = random.sample(tonight, 4)
		#mnu = "How about {}, and {}?".format(for t in tonight[0:-1], tonight[-1]) 
		mnu = "How about " + tonight[0] + ", " + tonight[1] + ", " + tonight[2] + ", and " + tonight[3] + "?"
		print(mnu)
		while 1:
			data  = recordAudio()
			data
			if data in nupe:
				print('Ok, trying again.')
			
			elif data in yip:
				s = open(shoppingList, 'a+')
				for i in tonight:
					s.write(i)
				s.close()
				tryAgain = False
				print('OK, added to the shopping list. Want me to send it now?')
				while 1:
					data = input('...')
					if data in yip:
						print('sending it now')
						shoppingList()
						break

					elif data in nupe:
						print('Ok then.')
						break
			elif 'keep' in data:
				data = data.split(' ')
				if 'and' in data:
					keep = data
			else:
				continue
			break

def ShoppingList():
	play(gotIt)
	play('Voiceverificationrequired.mp3')
	while 1:
		#data = recordAudio()
		data = input('1')
		data
		if data in emails.keys():
			play('accessgranted.flac')
			('Access granted..mp3')
			list = open(shoppingList, 'r+').readlines()
			items = ["\n    <li>{}</li>".format(s) for s in list]
			items = "".join(items)
			list1 = '''\
			<html>
			<head>
			</head>
			<ul style="font-family: trebuchet;">
			<h2>Hi! Here's the shopping list:</h2>
			<ul style="border: 1px solid black; padding: 40px;">
			{}
			</ul>
			</body>
			</html>
			'''.format(items)
			
			list1 = MIMEText(list1, 'html')
			email(email=emails.get(data), content=list1.as_string())
			play(firm)
		
		else:
			play('botwfail.flac')
			pass
		break
	
def weather(): #weather duh
	API_key = 'fc1e626cf9767a060d5f305178089700'
	cache = LRUCache()
	owm = OWM(API_key)
	obs = owm.weather_at_id(6183235)
	w = obs.get_weather()
	sky = w.get_detailed_status()
	temp = w.get_temperature(unit='celsius')
	tempnow = temp['temp']
	tempnow1 = str(tempnow)
	tempnow1.split('.')
	tempnow2 = int(tempnow1[0:2])
	speak('It\'s ' + str(tempnow2) + ' degrees with ' + sky)
	speak('Would you like to know more.')
	while 1:
		data = recordAudio()
		data
		data = data.split(' ')
		if 'yes' in data:
			hi = w.get_temperature(str(temp['temp_max']), unit='celsius')
			lo = w.get_temperature(str(temp['temp_min']), unit='celsius')
			if int(now.strftime('%H')) < 13: 
				speak('Today will reach a high of ' + str(hi) + ' with ' + w.get_clouds())
			else:
				speak('Tonight will reach a low of ' + str(lo) + ' with ' + w.get_clouds())
		else:
			speak('Moving on then.')
		break

def playMusic(): #play music from... play music.
	api = Mobileclient()
	api.search("token code red", max_results=1)
	
def wolframThisShit(): #catch all look shit up
	app_id = "HJVXH3-4XQ32P9PTJ"   #Put wolfram API here
	client = wolframalpha.Client(app_id)
	dataa = data.split(' ')
	dataa = dataa[3:]
	space = ' '
	q = space.join(dataa)
	res = client.query(q)
	answer = next(res.results).text
	speak(answer)

def googleSearch(): #for when wolfram fails
	options = Options()
	options.headless = True
	url = "https://www.google.com"
	browser = webdriver.Firefox(options=options)
	browser.get(url)
	searchbox = browser.find_element_by_name("q")
	searchbox.send_keys(data[3:])
	searchbox.submit()
	time.sleep(2)
	try:
		result = browser.find_element_by_class_name('Z0LcW')
		speak(result.text)
	except:
		speak('I can\'t find that')
		
def email(email, content):#catch all email function
	port = 465  # For SSL

	context = ssl.create_default_context() #create a secure SSL context
	list = open('shoppingList.txt').read()
	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
		server.login("thisisada69@gmail.com", "Coulson1")
		server.sendmail("thisisada69@gmail.com", email, content)
		server.close()
		
def addToList():
	list = open(shoppingList, 'a+')
	llst = data.split(" ")
	if 'and' in llst:
		del llst[0:4]
		thing = str(llst)
		thing = thing.split('and')
		for item in thing:
			list.write("%s\n" %item)
		play(firm)
		list.close()
		play(firm)
		pass
	else:
		thing = llst[4:]
		list.write("%s\n" %thing)
		speak("Added %s." %(thing))
		list.close()
		play(reply)
		
#==============================================================================#
#-----------------------Home automation----------------------------------------#
#==============================================================================#
def lightControl():
	lamp = ''
	tv = ''
	beacon = ''
	on = '/on'
	off = '/off'
	if 'lamp' in data:
		if 'turn on' in data:
			play(gotIt)
			requests.get(lamp + on)
		elif 'turn off' in data:
			play(gotIt)
			requests.get(lamp + off)
			
	elif 'tv' in data:
		if 'turn on' in data:
			play(gotIt)
			requests.get(tv + on)
		elif 'turn off' in data:
			play(gotIt)
			requests.get(tv + off)
			
	elif 'bedtime' in data:
		pass
		
	elif 'beacon' in data:
		pass
	
def castPause():
	mc.pause()
		
def castPlay():
	mc.play()
		
def setVol():
	data = data.split(' ')
	i = int(data[4])
	print(data)
	print('data:' + data[4])
	if i in range(100):
			i = i / 100
			print('i divided by 100: ' + i)
			cast.set_volume(i)
			print('volume:' + str(vol))
	else:
		play(fail)
			
def volUp():
		if vol < 1.0:
			cast.set_volume(vol + 0.2)
			print('vol:' + str(vol))
		else:
			play(fail)
def volDown():
		if vol > 0.0:
			cast.set_volume(vol - 0.2)
			print(vol)
		else:
			play(fail)
						
def volLevel():
		speak(str(vol * 100) + ' percent') 
		print(vol)
			
	
#==============================================================================#		
#-------------------------Do shit----------------------------------------------#
#==============================================================================#

def ada(data):
	talk = os.chdir('./audio')
	dtalk = os.chdir('..')
	reply = './audio/replies/' + random.choice(os.listdir('./audio/replies/'))
	now = datetime.now()
	e = 'Ada '
	check = ['Ada you there', 'Ada you up', 'Oh Ada']
	#try:
	if data in check:
		play(gotIt)
		morn = play('./audio/Goodmorning..mp3 ')
		aft = play('./audio/Goodafternoon..mp3')
		eve = play('./audio/Goodevening.mp3')
		i = ''
		f = int(now.strftime('%H'))
		if f in range(4, 11):
			i= morn
		elif f in range(12, 16):
			i = aft
		elif f in range(17, 24):
			i = eve
		else:
			i = play('You\'re up late..mp3')

		# called.write('1')
		# if called.read() != '0':
		# 	e = ''
		# 	called.close()
		# else:
		# 	e = "Ada "
		# 	called.write('0')

		pass
		
#----------Info----------------------------------------------------------------#
		
	elif e + "what time is it" in data:
		play(gotIt)
		speak("It's " + now.strftime('%-I:%-M'))
		pass

	elif e + "tell me" in data:
		play(gotIt)
		try:
			wolframThisShit()
		except:
			speak('Nothing found. Want me to google it?')
			while 1:
				data = recordAudio()
				data
				data = data.split()
				if data == 'Yes':
					try:
						googleSearch()
					except:
						speak('Sorry, nothing found.')
	#elif e _ 'where am I' in data:
	
#----------Media---------------------------------------------------------------#

	elif e + 'set volume to' in data:
		setVol()
		
	elif e + 'turn it up' in data:
		volUp()
	
	elif e + 'turn it down' in data:
		volDown()
		
	elif e + 'how loud' in data:
		volLevel()
		
	elif e + 'press play' in data:
		castPlay()
		
	elif e + 'pause' in data:
		castPause()
		
#----------Food & shopping-----------------------------------------------------#
	
	elif e + "there\'s no more" in data:
		play(gotIt)
		addToList()
		
	elif e + "send the shopping list" in data:
		ShoppingList()

	elif e + 'meal plan time' in data:
		play(gotIt)
		forDinner()
		
#----------Misc----------------------------------------------------------------#

	elif e + "initiate Lazarus protocol" in data:
		play(gotIt)
		email(email='monkay03@hotmail.com', content='<3')
		speak("Lazarus protocol initiated")

	elif e + 'flip a coin' in data:
		while 1:
			coin = []
			coin = random.choice(['heads.mp3', 'tails.mp3'])
			time.sleep(3)
			talk
			speak(coin)
			play('Goagain?.mp3')
			dtalk
			data = recordAudio()
			data
			data = data.split(' ')
			if data in yip:
				continue
			elif data in nupe:
				talk
				play('Finethen.mp3')
				dtalk
			break						
		
	elif e + 'what\'s it like out' in data:
		play(gotIt)
		weather()

		
	elif e + 'bedtime' in data:
		requests.get('https://192.168.100.124/RELAY=ON')
		
	elif e + 'execute protocol Foxtrot Unicorn Charlie Kilo':
		pass
				
	elif data == 'exit':
		sys.exit()
		
	else:
		# called.write('0')
		# called.close()
		pass
	#except:
		#play('botwfail.flac')
	#	pass
			
#==============================================================================#
#--------------------------initialization--------------------------------------#
#==============================================================================#

time.sleep(2)
play('./audio/sys/startup.ogg')

chromecasts = pychromecast.get_chromecasts() #start chromecast control
[cc.device.friendly_name for cc in chromecasts]
cast = next(	cc for cc in chromecasts if cc.device.friendly_name == 'Family room TV')
cast.wait()
mc = cast.media_controller
vol = cast.status.volume_level

# proc = [] #gather processes for startup
# for process in tqdm(psutil.process_iter()):
# 	proc.append(process.cmdLine())
# 	print(process.ccmdLine())	
# startup = ['python3', 'startup.py']
# if startup not in  proc:
# 	Popen(startup)
# else:
# 	pass


	
while 1:
	reply = ''
	#data = recordAudio()
	data = input('What?')
	ada(data)
	