import random
shoppingList = 'shoppingList.txt'
menu = {
'Roast Chicken':
'Chicken\n',

'Burritos':
'Cheese\n'
'Wraps\n'
'Refried beans\n'
'Mexican rice\n'
'Canned corn\n'
'Chicken\n'
'Taco seasoning\n',

'Enchiladas':
'Cheese\n'
'Chicken\n'
'Wraps\n'
'Tomato sauce\n'
'Chicken stock\n'
'Taco seasoning\n',

'Sheperds pie':
'Potatoes\n'
'Ground beef\n'
'Creamed corn\n'
'Veggies\n'
'Brown gravy\n'
'Milk\n',

'Metloaf':
'Eggs\n'
'Breadcrumbs or ShakenBake mix\n'
'Ground beef\n'
'BBQ sauce\n',

'Stir fry':
'Veggies\n'
'Rice\n'
'Eggs\n'
'Soy sauce\n'
'Hot sauce\n'
'Meat\n',

'Quesadillas':
'Wraps\n'
'Cheese\n'
'Meat\n'
'Taco seasoning\n',

'Mac n cheese':
'Pasta\n'
'Cheese\n'
'Milk\n'
'Flour\n'
'Additions for mac n cheese(Bacon, meat, veggies, etc)\n',

'Smokies':
'Smokies\n'
'Buns\n',

'Burgers':
'Buns\n'
'Ground beef\n'
'Tomatoes\n'
'Lettuce\n'
'Eggs\n'
'Garlic powder\n'
'Milk\n'
'Crackers\n',

'Peanut chicken stir fry':
'Peanuts\n'
'Peanut butter\n'
'Sriracha\n'
'Lime\n'
'Rice\n'
'Vegetable'
}
def forDinner():	
	dinners = []
	addtoList = []
	starch = ['roasted potatoes', 'rice', 'perogies', 'mashed potatoes', 'fries']
	veg = ['roasted carrots', 'frozen veg', 'honey carrots']
	lest = open(shoppingList, 'a+')
	tinight = menu.keys()
	tonight = random.sample(tinight, 3)
	for item in tonight:
		if 'no side' not in  menu.get(item):
			dinners.append(item + ' with ' + random.choice(starch) + ' and ' + random.choice(veg))
		else:
			dinners.append(item)
	for item in tonight:        
		if item not in lest:
			addtoList.append(item)	
		else:
			pass		
	print('added to the shopping list')
	print(dinners[0] + ", " + dinners[1] + ' and ' + dinners[2] + ' have been chosen and added to the list.')
	#lest.close()
	for item in tonight:	
		lest.write(menu.get(item))
	lest.close()
forDinner()