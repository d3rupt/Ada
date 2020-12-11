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
from gmusicapi import Mobileclient, Musicmanager
import vlc
from google_music import MobileClient
import _thread
#==============================================================================#
#----------------------Database------------------------------------------------#
#==============================================================================#

emails = {
'Otis':'monkay03@hotmail.com',
'me': 'thdnkns@gmail.com'
}

menu = {

'chicken':
'chicken\n\n',

'burritos':
['cheese\n',
'wraps\n',
'refried beans\n',
'mexican rice\n',
'canned corn\n',
'chicken\n',
'taco seasoning\n'],

'enchiladas':
['cheese\n',
'chicken\n',
'wraps\n',
'tomato sauce\n',
'chicken stock\n',
'taco seasoning\n'
],

'shepherds pie':
['potatoes\n',
'ground beef\n',
'creamed corn\n',
'veggies\n',
'brown gravy\n',
'milk\n'
],

'meatloaf':
['eggs\n',
'breadcrumbs or ShakenBake mix\n',
'ground beef\n',
'bbq sauce\n'],

'stir fry':
['veggies\n',
'rice\n',
'eggs\n',
'soy sauce\n',
'hot sauce\n',
'meat\n'
],

'quesadillas':
['wraps\n',
'cheese\n',
'meat\n',
'taco seasoning\n'
],

'mac and cheese':
['pasta\n',
'cheese\n',
'milk\n',
'flour\n',
'additions (bacon, meat, veggies, etc)\n'
],


'smokies':
['smokies\n',
'buns\n'
],

'burgers':
['buns\n',
'ground beef\n',
'tomatoes\n',
'lettuce\n',
'eggs\n',
'garlic powder\n'
],

'peanut chicken stir fry':
['peanut butter\n',
'sriracha\n',
'lime\n',
'rice\n',
'vegetable\n',
'garlic\n'
],

'hot dogs':
['hot dog buns\n',
'hot dogs\n'
],

'pork with apple sauce':
['pork\n',
'apple juice or apples\n',
'thyme\n'
'butter\n',
'stock\n'],

'taco salad':
['lettuce\n',
'tomato\n',
'cheese\n',
'catalina\n',
'ground beef\n',
'tostitos\n',
'avocado\n'
],

'thai curry':
['vegetables\n',
'curry paste\n',
'stock\n',
'chicken, pork, chickpeas or cauliflower\n',
'coconut milk\n',
'rice\n',
'lime\n'
],

'shake and bake':
['chicken or pork\n',
'shaneNbake mix\n'],

'spaghetti':
['ground beef\n',
'tomato sauce\n',
'mushrooms\n',
'pasta\n',
'onions'],

'pizza':
['tomato sauce\n',
'cheese\n',
'toppings\n',
'flour\n',
'yeast\n']

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
	data = "".lower()
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
	os.system('mpg321 {}'.format(sound))

def deeper():
	data  = recordAudio()
	while 1:
		data

def forDinner():	 #meal planning
	tryAgain = True
	tonight = []
	tonight = menu.keys()
	tonight = random.sample(tonight, 4)
	while tryAgain == True:
		#mnu = "How about {}, and {}?".format(for t in tonight[0:-1], tonight[-1])
		mnu = "How about " + tonight[0] + ", " + tonight[1] + ", " + tonight[2] + ", and " + tonight[3] + "?"
		print(mnu)
		while 1:
			#data  = recordAudio()
			data = input('...')
			data
			if data in nupe:
				print('Ok, trying again.')

			elif data in yip:
				s = open(shoppingList, 'a+')
				for i in tonight:
					s.write(i + ':\n\n')
					for j in menu.get(i):
						s.write(j)
				s.close()
				tryAgain = False
				print(reply + ' Want me to send it now?')
				while 1:
					data = input('...')
					if data in yip:
						print(reply)
						ShoppingList()
						break

					elif data in nupe:
						print(reply)
						break

			elif 'keep' in data:
				choice = list(menu.keys())
				for t in tonight:
					if t in data:
						pass
					else:
						tonight.remove(t)

				while len(tonight) < 4:
					choice1 = ''
					choice1 = random.choice(choice)
					print(' chose ' + choice1)
					if choice1 not in tonight:
						tonight.append(choice1)
						print('appended ' + choice1)
					else:
						pass

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
			play(reply)

		else:
			play('botwfail.flac')
			pass
		break

def weather(): #weather duh
	API_key
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
	app_id = ""   #API KEY
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
		server.login("", "")
		server.sendmail("", email, content)
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
		thing = llst[3:]
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
		elif 'daylight' or 'day light' in data:
			play(gotIt)
			requests.get(lamp + '/daylight')

	elif 'tv' in data:
		if 'turn on' in data:
			play(gotIt)
			requests.get(tv + on)
		elif 'turn off' in data:
			play(gotIt)
			requests.get(tv + off)

	elif 'bedtime' in data:
		time.sleep(2)
		requests.get(tv + off)
		time.sleep(2)
		requests.get(lamp + off)
		pass

	# elif 'beacon' in data:
	# 	if 'light the beacon' in data:
	# 		requests.get(beacon)
	#
	# 	elif 'extinguish the beacon' in data:
	# 		requests.get(beacon + off)
	#
	# 	elif 'color the beacon' in data:
	# 		if 'ice' in data:
	# 			requests.get(beacon + '/ice')
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

def music(data):
	data = data.split(' ')
	global p
	p  = vlc.MediaPlayer()
	playing = 'State.Playing'
	gmmc = MobileClient('')
	gmmc.login('')
	songs = []
	length = []
	songdict = {}
	srch = gmmc.search_google(data)
	if 'play' in data:
		data = data[1:]
		artist = srch['artists'][0]
		songlist = gmmc.shuffle_artist(artist, num_songs=100, only_artist=True)
	elif 'play' in data and data[-1] == 'mix':
		data = data[1:-2]
		artist = srch['artists'][0]
		songlist = gmmc.shuffle_artist(artist, num_songs=100)
	elif data[-1] == 'music':
		data = data[1:-2]
		genre = srch['genres'][0]
		songlist = gmmc.shuffle_genre(genre)
	for s in songlist:
		songs.append(s['storeId'])
		length.append(int(s['durationMillis']) / 1000 + 5)
	for s, l in zip(songs, length):
		songdict[s] = l
	gmmc.logout()

	apimc = Mobileclient('')
	mmc = Musicmanager('')
	apimc.oauth_login('')

	songs = []
	length = []
	songdict = {}
	srch = gmmc.search_google(data)
	if 'play' in data:
		data = data[1:]
		artist = srch['artists'][0]
		songlist = gmmc.shuffle_artist(artist, num_songs=100, only_artist=True)
	elif 'play' in data and data[-1] == 'mix':
		data = data[1:-2]
		artist = srch['artists'][0]
		songlist = gmmc.shuffle_artist(artist, num_songs=100)
	elif data[-1] == 'music':
		data = data[1:-2]
		genre = srch['genredio = mmc.download_song(s)

	for song in songdict:
		p.audio_set_volume(75)
		print(song)
		print(songdict[song])
		url = apimc.get_stream_url(song)
		print(url)
		p.set_mrl(url)
		p.play()
		global state
		state = str(p.get_state())
		while state != 'State.Ended' or state != 'State.Stopped':
			state = ''
			state = str(p.get_state())
			pass
		print('ended')
		time.sleep(1.5)

	apimc.logout()
	mmc.logout()

#==============================================================================#
#-------------------------Do shit----------------------------------------------#
#==============================================================================#

def ada(data):
	talk = os.chdir('./audio')
	dtalk = os.chdir('..')
	reply = './audio/replies/' + random.choice(os.listdir('./audio/replies/'))
	now = datetime.now()
	e = 'ada'
	# check = ['Ada you there', 'Ada you up', 'Oh Ada']
	# #try:
	# if data in check:
	# 	play(gotIt)
	# 	morn = play('./audio/Goodmorning..mp3 ')
	# 	aft = play('./audio/Goodafternoon..mp3')
	# 	eve = play('./audio/Goodevening.mp3')
	# 	i = ''
	# 	f = int(now.strftime('%H'))
	# 	if f in range(4, 11):
	# 		i= morn
	# 	elif f in range(12, 16):
	# 		i = aft
	# 	elif f in range(17, 24):
	# 		i = eve
	# 	else:
	# 		i = play('You\'re up late..mp3')

	if e in data:
		try:
			p.pause()
		except:
			pass
		data = input('What? part deux\n')

#----------Info----------------------------------------------------------------#

		if "what time is it" in data:
			play(gotIt)
			speak("It's " + now.strftime('%-I:%-M'))
			pass

		elif "tell me" in data:
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

		elif 'set' in data and 'volume' in data:
			setVol()

		elif 'turn up' in data:
			if 'tv' in data:
				c = cast.status
				c = c.split(',')
				c= c[12].split('=')
				if c[1] != '':
					volUp()
				else:
					pass
			elif 'music' in data:
				state = ''
				state = str(p.get_state)
				if state == playing:
					p.audio_set_volume(p.audio_get_volume() + 10	)
				else:
					pass
			else:
				play(fail)

		elif 'turn it down' in data:
			if 'tv' in data:
				c = cast.status
				c = c.split(',')
				c= c[12].split('=')
				if c[1] != '':
					volDown()
				else:
					pass
			elif 'music' in data:
				state = ''
				state = str(p.get_state)
				if state == playing:
					p.audio_set_volume(p.audio_get_volume() - 10	)
				else:
					pass
			else:
				play(fail)

		elif 'press play' in data:
			if 'tv' in data:
				castPlay()
			elif 'music' in data:
				p.play()
			else:
				pass

		elif 'pause' in data:
			if 'tv' in data:
				castPause()
			elif 'music' in data:
				p.pause()
			else:
				pass

		elif 'play' in data:
			musicThread = _thread.start_new_thread(music, (data,))

		elif 'skip' in data:
			p.stop()


	#----------Food & shopping-----------------------------------------------------#

		elif "there\'s no more" in data:
			play(gotIt)
			addToList()

		elif 'what\'s on the shopping list'
		elif "send the shopping list" in data:
			ShoppingList()

		elif 'meal planner' in data:
			play(gotIt)
			forDinner()

	#----------Misc----------------------------------------------------------------#

		elif "initiate Lazarus protocol" in data:
			play(gotIt)
			email(email='monkay03@hotmail.com', content='<3')
			speak("Lazarus protocol initiated")

		elif 'flip a coin' in data:
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

		elif 'what\'s it like out' in data:
			play(gotIt)
			weather()


		elif 'bedtime' in data:
			requests.get('https://192.168.100.124/RELAY=ON')

		elif 'execute protocol Foxtrot Unicorn Charlie Kilo':
			pass

		elif data == 'exit':
			sys.exit()

		elif 'nevermind' in data:
			pass

		else:
			pass

	time.sleep(1)
	p.play()
	print('play')

		#except:
			#play('botwfail.flac')
		#	pass

#==============================================================================#
#--------------------------initialization--------------------------------------#
#==============================================================================#

time.sleep(2)
#play('./audio/sys/startup.mp3')

# chromecasts = pychromecast.get_chromecasts() #start chromecast control
# [cc.device.friendly_name for cc in chromecasts]
# cast = next(	cc for cc in chromecasts if cc.device.friendly_name == 'Family room TV')
# cast.wait()
# mc = cast.media_controller
# vol = cast.status.volume_level

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
