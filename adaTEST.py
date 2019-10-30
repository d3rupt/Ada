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
#import gmusicapi
#import forDinner as menu
from playsound import playsound
#from flask import Flask
from datetime import datetime
from pyowm import OWM
from pyowm.caches.lrucache import LRUCache
from email.mime.text import MIMEText
#import psutil
from tqdm import tqdm
#app = Flask(__name__)

#==============================================================================#
#----------------------Database------------------------------------------------#
#==============================================================================#

shoppingList = 'shoppingList.txt'
now = datetime.now()

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
	os.system('mpg321 {}'.format(sound))
def deeper():
	data  = recordAudio()
	while 1:
		data
	return data
def forDinner():	 #meal planning
	dinners = []
	lest = open(shoppingList, 'a+')
	tinight = menu.keys()
	tonight = random.sample(tinight, 3)
	for item in tonight:
		summer, starch, veg = []
		it = menu.get(item)
		print(it)
		
		if 'no side\n\n' in it:
			print('True')
			dinners.append(item)	
			lest.write('%s:\n' %item)
			for i in it[0:-1]:	
				lest.write(i + '\n' + '\ n')
				
		elif 'summer\n\n' in it:
			summer = ['fries', 'roasted potatoes', 'potato salad', 'salad']
			print('True')
			dinners.append(item + ' with ' + choice(summer) )	
			lest.write('%s:\n' %item)
			for i in tqdm(it[0:-1]):	
				lest.write(i)
			lest.write('side: ' + summer + '\n' + '\n')
			
		else:
			starch = random.choice(['roasted potatoes', 'rice', 'perogies', 'mashed potatoes', 'fries', 'potato salad'])
			veg = random.choice(['roasted carrots', 'frozen veg', 'honey carrots', 'corn', 'green beans', 'asparagus', 'salad', 'coleslaw'])
			dinners.append(item + ' with ' + starch + ' and ' + veg)
			lest.write('%s:\n' %item)
			for i in it[0:-1]:
				lest.write(i)
			lest.write('side: ' + starch + '\n')
			lest.write('side: ' + veg + '\n' + '\n')
	print('added to the shopping list')
	speak(dinners[0] + ", " + dinners[1] + ' and ' + dinners[2] + ' have been chosen and added to the list.')
	for item in tqdm(tonight):	
		lest.write(menu.get(item))
	lest.close()
	
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
		
#==============================================================================#
#-----------------------Home automation----------------------------------------#
#==============================================================================#
		
#==============================================================================#		
#-------------------------Do shit----------------------------------------------#
#==============================================================================#


def ada(data):
	e = "Ada "
	ifcalled = 0
	now = datetime.now()
	firm = ''
	firm = random.choice(con)
	check = ['Ada', 'Ada you there', 'Ada you up', 'Oh Ada']
	#try:
	if data in check:
		play('light.ogg')
		morn = play('Good morning..mp3 ')
		aft = play('Good afternoon..mp3')
		eve = play('Good evening.mp3')
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
			
		greeting = ["What can I do?.mp3", "Make it quick, I'm busy..mp3"]
		play(i)
		play(random.choice(greeting))
		
		ifcalled +=1
		if ifcalled != 0:
			e = ''
		pass
		
	elif e + 'go f*** yourself' in data:
		speak('Fuck you cunt, you wanna go')
		
	elif e + 'flip a coin' in data:
		while 1:
			coin = []
			coin = random.choice(['heads', 'tails'])
			time.sleep(3)
			speak(coin)
			play('Goagain?.mp3')
			data = recordAudio()
			data
			data = data.split(' ')
			if 'yes' in data:
				continue
			elif 'no' in data:
				play('Finethen.mp3')
			break
		
	elif e + "how are you" in data:
		play('light.ogg')
		reply = ["I'm fine.", "could be better.", "fuck off."]
		speak(random.choice(reply) + ' What can i do for you?')
		pass

	elif e + "what time is it" in data:
		play('light.ogg')
		speak("It's " + time.ctime())
		pass

	#elif e _ 'where am I' in data:
	
	elif e + "where\'s" in data:
		play('light.ogg')
		data = data.split(" ")
		location = data[2:-1]
		speak("Hold on, I 'll show you where " + location + " is.")
		os.system("mozilla-browser https://www.google.ca/maps/place/" + location + "/&amp;")
		pass
	
	elif e + "who are you" in data:
		play('light.ogg')
		speak("I am Ada, personal assistant to this family. %s" %random.choice(['Heil Hydra.', 'Why are you bothering me?', 'Under his eye.']))
		pass
		
	elif e and "there\'s no more" in data:
		play('light.ogg')
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
			speak("Added %s. %s" %(thing, firm))
			list.close()
			play(firm)
		
	elif e + "send the shopping list" in data:
		play('light.ogg')
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
		
	elif e + "initiate Lazarus protocol" in data:
		play('light.ogg')
		email(email='monkay03@hotmail.com', content='<3')
		speak("Lazarus protocol initiated")
		
	elif e + "convert" in data:
		play('light.ogg')
		speak(random.choice(con))
		data = data.split(" ")
		googleSearchConvert()
		
	elif e + "tell me" in data:
		play('light.ogg')
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
				
	elif e + "play" in data:
		play('light.ogg')
		data = data.split(" ")
		
	elif e + 'what\'s it like out' in data:
		play('light.ogg')
		weather()

		
	elif e + 'meal plan time' in data:
		play('light.ogg')
		forDinner()
		
	elif e + 'bedtime' in data:
		print('Hello Dae')
		requests.get('https://192.168.100.124/RELAY=ON')
		
	elif e + 'execute protocol Foxtrot Unicorn Charlie Kilo':
		pass
				
	elif data == 'exit':
		sys.exit()
		
	else:
		if iss == 1:
			play('error.mp3')
			pass
		else:
			pass
	#except:
		#play('botwfail.flac')
	#	pass
			
#==============================================================================#
#--------------------------initialization--------------------------------------#
#==============================================================================#

time.sleep(2)
play('startup.ogg')	
con = []
for file in os.listdir('./replies'):
	con.append(file)
#	for process in tqdm(psutil.process_iter()):
#		if process.cmdline() != ['python3', 'initi.py']:
#			Popen(['python3', 'initi.py'])
#		else:
#			pass
while 1:
	iss = 0
	#data = recordAudio()
	data = input('What?')
	ada(data)
	