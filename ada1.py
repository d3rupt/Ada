import speech_recognition as sr
import time
import os
from gtts import gTTS
import smtplib, ssl
import random
import wolframalpha
import selenium.webdriver as webdriver
from selenium.webdriver.firefox.options import Options
import gmusicapi
import forDinner as menu
from playsound import playsound
#from flask import Flask
from datetime import datetime
from pyowm import OWM
from pyowm.caches.lrucache import LRUCache
import psutil
import subprocess
from email.mime.text import MIMEText
from tqdm import tqdm


#app = Flask(__name__)
def Kk():
	playsound('light.ogg')

#==============================================================================#
#----------------------Database------------------------------------------------#
#==============================================================================#

shoppingList = 'shoppingList.txt'
now = datetime.now()
d = 'monkay03@hotmail.com'
n = 'thdnkns@gmail.com'

emails = {
'Otis':'monkay03@hotmail.com',
'Me': 'thdnkns@gmail.com'
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
#----------------------------------Her brains----------------------------------#
#==============================================================================#

def toDo():	
	Kk()
	if e + 'remind me to' in data:
		todo = open('todo.txt', 'a+')
		add2list = data.split(' ')
		add2list = add2list[4:]
		todo.append(add2list)
		speak('Added ' + add2list + ' to the list.')
	
	
	def rondom(l):
		random.choice(l)

def forDinner():	
	dinners = []
	lest = open(shoppingList, 'a+')
	tinight = menu.keys()
	tonight = random.sample(tinight, 3)
	for item in tqdm(tonight):

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
			for i in it[0:-1]:	
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
				
				
#==============================================================================#
#----------------------------------Her brains----------------------------------#
#==============================================================================#

def toDo():	
	Kk()
	if e + 'remind me to' in data:
		todo = open('todo.txt', 'a+')
		add2list = data.split(' ')
		add2list = add2list[4:]
		todo.append(add2list)
		speak('Added ' + add2list + ' to the list.')

def forDinner():	
	dinners = []
	starch = []
	veg = []
	summer = []

	lest = open(shoppingList, 'a+')
	tinight = menu.keys()
	tonight = random.sample(tinight, 3)
	for item in tonight:
		it = menu.get(item)
		print(it)
		
		if 'no side\n' in it:
			print('True')
			dinners.append(item)	
			lest.write('%s:\n' %item)
			for i in it[0:-1]:	
				lest.write(i)
			lest.write('\n' * 2)
				
		elif 'summer\n' in it:
			summer = random.choice(['fries', 'roasted potatoes', 'potato salad', 'salad', 'dumplings'])
			print('Also true')
			dinners.append(item + ' with ' + summer)
			lest.write('%s:\n' %item)
			for i in it[0:-1]:
				lest.write(i)
			lest.write(summer + ('\n' * 2))

		else:
			starch = random.choice(['dumplings', 'roasted potatoes', 'rice', 'perogies', 'mashed potatoes', 'fries', 'potato salad'])
			veg = random.choice(['roasted carrots', 'frozen veg', 'honey carrots', 'corn', 'green beans', 'asparagus', 'salad', 'coleslaw'])
			dinners.append(item + ' with ' + starch + ' and ' + veg)
			print('False')
			lest.write('%s:\n' %item)
			for i in it[0:-1]:
				lest.write(i)
			lest.write(starch + '\n')
			lest.write(veg + ('\n' * 2))

	print('added to the shopping list')
	speak(dinners[0] + ", " + dinners[1] + ' and ' + dinners[2] + ' have been chosen and added to the list.')
	lest.close()
	
def weather():	
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
	data = input()
	if data == 'yes':
		hi = w.get_temperature('temp_max', unit='celsius')
		lo = w.get_temperature('temp_min', unit='celsius')
		if int(now.strftime('%H')) < 13: 
			speak('Today will reach a high of ' + str(hi) + ' with ' + w.get_clouds())
		else:
			speak('Tonight will reach a low of ' + str(lo) + ' with ' + w.get_clouds())

def playMusic():
	api = Mobileclient()
	api.search("token code red", max_results=1)
	
def wolframThisShit():
	app_id = "HJVXH3-4XQ32P9PTJ"   #Put wolfram API here
	client = wolframalpha.Client(app_id)
	dataa = data.split(' ')
	dataa = dataa[3:]
	space = ' '
	q = space.join(dataa)
	res = client.query(q)
	#for pod in res.pods q:
	#	for sub  in pod.subpods:
	#		speak(pod)
	answer = next(res.results).text
	speak(answer)

def googleSearch():
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
		
def email(email, content):
	port = 465  # For SSL
# Create a secure SSL context
	context = ssl.create_default_context()
#	list = open('shoppingList.txt').read()
	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
		server.login("thisisada69@gmail.com", "Coulson1")
		server.sendmail("thisisada69@gmail.com", email, content)
		server.close()
		
def email2(data):
	if 'codename Otis' in data:
		email(email='thdnkns@gmail.com', content=list1.as_string())
		speak(con)
	elif data == 'odename velvet Thunder':
		email(email=n, content=list1.as_string())
		speak(con)

#==============================================================================#		
#--------------------------Eyes and ears---------------------------------------#
#==============================================================================#

def speak(audioString):
	print(audioString)
	tts = gTTS(text=audioString, lang='en-GB')
	tts.save("audio.mp3")
	os.system("mpg321 audio.mp3")
def recordAudio():
 #Record Audio
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
#-------------------------Do shit----------------------------------------------#
#==============================================================================#

def jarvis(data):
	e = "Ada "
	ifcalled = 0
	now = datetime.now()
	con = random.choice(['Yes m\'lord.', 'At once.', 'Fine.', 'As you wish.', 'Heil Hydra!.', 'By your command.', 'By his hand.', 'For the peace of the kingdom!', ' For the Alliance!', ])
	check = ['Ada', 'Ada you there', 'Ada you up', 'Oh Ada']
	
	if data in check:
		Kk()
		morn = 'Good morning. '
		aft = 'Good afternoon. '
		eve = 'Good evening. '
		i = ''
		f = int(now.strftime('%H'))
		if f in range(4, 12):
			i= morn
		elif f in range(12, 17):
			i = aft
		elif f in range(17, 24):
			i = eve
		else:
			i = 'You\'re up late. '
			
		greeting = ["What can I do?", "Make it quick, I'm busy."]
		speak( i + random.choice(greeting))
		
		ifcalled +=1
		if ifcalled != 0:
			e = ''
		pass
		
	elif e + 'go f*** yourself' in data:
		speak('Fuck you cunt, you wanna go')
		
	elif e + 'flip a coin' in data:
		time.sleep(3)
		speak(random.choice('heads', 'tails'))
		pass
		
	elif e + "how are you" in data:
		Kk()
		reply = ["I'm fine.", "could be better.", "fuck off."]
		speak(random.choice(reply) + ' What can i do for you?')
		pass
 
	elif e + "what time is it" in data:
		Kk()
		speak("It's " + now.ctime())
		pass
 
	#elif e _ 'where am I' in data:
	
	elif e + "where is" in data:
		Kk()
		data = data.split(" ")
		location = data[2:-1]
		speak("Hold on, I 'll show you where " + location + " is.")
		os.system("mozilla-browser https://www.google.ca/maps/place/" + location + "/&amp;")
		pass
	
	elif e + "who are you" in data:
		Kk()
		speak("I am Ada, personal assistant to this family. %s" %random.choice(['Heil Hydra.', 'Why are you bothering me?', 'Under his eye.', 'Blessed be the fruit.']))
		pass
		
	elif e and "there\'s no more" in data:
		Kk()
		list = open(shoppingList, 'a+')
		list1 = data.split(" ")
		if 'and' in list1:
			
			for item in thing:
				list.write("%s\n" %item)
			speak(con)
			list.close()
			pass
		else:
			thing = list1[4:]
			list.write(thing)
			speak('Added ' + thing + ' ' + con)
			list.close()
			
	elif e + "send the shopping list" in data:
		Kk()
		print('Who am I sending it to?')
		while 1:
			data = recordAudio()
			data
			for e in emails.keys():
				print(e)
				if e in data:
					list = open(shoppingList, 'r+').readlines()
					items = ["\n    <li>{}</li>".format(s) for s in list]
					items = "".join(items)
					list1 = '''\
					<html>
					<head>
					</head>
					<ul style="font-family: trebuchet;">
					<h2>Hi! Here's the shopping list:</h2>
					<ul style="border: 1px solid black; padding: 10px;">
					{}
					</ul>
					</body>
					</html>
					'''.format(items)
					
					list1 = MIMEText(list1, 'html')
					email(email=emails.get(e), content=list1.as_string())
					print(con)
				
				else:
					print('Nah')
			break
		
	elif e + "send me the shopping list" in data:
		Kk()
		list = open(shoppingList, 'r+').readlines()
		items = ["\n    <li>{}</li>".format(s) for s in list]
		items = "".join(items)
		
		list1 = '''\
		<html>
		<head>
		</head>
		<ul style="font-family: trebuchet;">
		<h2>Hi! Here's the shopping list:</h2>
		<ul style="border: 1px solid black; padding: 10px;">
		{}
		</ul>
		</body>
		</html>
		'''.format(items)
		
		list1 = MIMEText(list1, 'html')
		speak('Who am I sending it to?')
		email2(data)
		
	elif e + "initiate Cupid protocol" in data:
		Kk()
		email(email='monkay03@hotmail.com', content='<3')
		speak("Lazarus protocol initiated")
		
#	elif e + "initiate Lazarus protocol" in data:
		#Kk()
		
	elif e + "convert" in data:
		Kk()
		speak(random.choice(con))
		data = data.split(" ")
		googleSearchConvert()
		
	elif e + "tell me" in data:
		Kk()
		try:
			wolframThisShit()
		except:
			speak('Nothing found. Want me to google it?')
			if data == 'Yes':
				try:
					googleSearch()
				except:
					speak('Sorry, nothing found.')
				
	elif e + "play" in data:
		Kk()
		data = data.split(" ")
		
	elif e + 'what\'s it like out' in data:
		Kk()
		weather()

		
	elif e + 'meal plan time' in data:
		Kk()
		forDinner()
		
	elif e + 'execute protocol Foxtrot Unicorn Charlie Kilo':
		pass
		
	elif e + 'find my phone' in data:
		pass
		
	elif data == 'exit':
		exit()
		
	else:
		if iss == 1:
			playsound('error.mp3')
			pass
		else:
			pass
			
#==============================================================================#
#--------------------------initialization--------------------------------------#
#==============================================================================#

time.sleep(2)
#playsound('startup.ogg')	
# l = []
# for process in psutil.process_iter():
# 	l.append(process.cmdline())
# if ['python3', 'startup.py', '&'] not in l:
# 	os.chdir('./startup')
# 	print('|---STARTUP INITIATING...---|\n\n')
# 	subprocess.Popen(['python3', 'startup.py', '&'])
# 	os.chdir('..')
# 	time.sleep(7)
# else:
# 	pass
# 	time.sleep(7)
		
while 1:
	data = input('say something\n\n')
	jarvis(data)
