from sqlalchemy import func

import requests
from pprint import pprint


from model import Styles, Category, Yeast, Hops, Fermentables, connect_to_db, db
from server import app

def load_styles():
	"""Load styles from api. Once its all figured out dump into a seed file."""

	#pulls data directly from api right now. 
	#want to change this to a seed file at a later time
	# r = requests.get(
 #    	"http://api.brewerydb.com/v2/styles?key=391f6548d25f4637ed5fb02c80236aad&")

	# styles = r.json()
	# styles = styles.values()
	# styles = styles[2]

	# for i, row in enumerate(styles):
	# 	if 'description' in row:
	# 		name = row['name']

	# 		if 'description' in row:
	# 			description = row['description']

	# 		if 'abvMin' in row:
	# 			abvMin = row['abvMin']
	# 		else:
	# 			abvMin = 0

	# 		if 'abvMax' in row:
	# 			abvMax = row['abvMax']
	# 		else:
	# 			abvMax = 0
	# 		if 'ibuMin' in row:
	# 			ibuMin = row['ibuMin']
	# 		else:
	# 			ibuMin = 0

	# 		if 'ibuMax' in row:
	# 			ibuMax = row['ibuMax']
	# 		else:
	# 			ibuMax = 0

	# 		if 'ogMin' in row:
	# 			ogMin = row['ogMin']
	# 		else:
	# 			ogMin = 0

	# 		if 'ogMax' in row:
	# 			ogMax = row['ogMax']
	# 		else:
	# 			ogMax = 0

	# 		if 'fgMin' in row:
	# 			fgMin = row['fgMin']
	# 		else:
	# 			fgMin = 0

	# 		if 'fgMax' in row:
	# 			fgMax = row['fgMax']
	# 		else:
	# 			fgMax = 0

	# 		if 'srmMin' in row:
	# 			srmMin = row['srmMin']
	# 		else:
	# 			srmMin = 0

	# 		if 'srmMax' in row:
	# 			srmMax = row['srmMax']
	# 		else:
	# 			srmMax = 0

	# 		if 'category' in row:
	# 			category = row['category']['name']
	# 		else:
	# 			category = ""
	# 	else:
	# 		continue

	# 	# pprint(row)

	# 	styles = Styles(name=name, description=description, abvMin=abvMin, 
	# 					abvMax=abvMax, ibuMin=ibuMin, ibuMax=ibuMax,
	# 					ogMin=ogMin, ogMax=ogMax, fgMin=fgMin, fgMax=fgMax,
	# 					srmMin=srmMin, srmMax=srmMax, category=category)
	# 	db.session.add(styles)

	# #returning a value error when trying to create a database from the
	# #styles.sql file. Will need to fix. But the api pull works.

	# for i, row in enumerate(open("seed_data/styles.sql")):
	# 	row = row.rstrip()

	# 	name, description, abvMin, abvMax, ibuMin, ibuMax, ogMin, ogMax, fgMin, fgMax, srmMin, srmMax, category = row.split("|")[1:]

	# 	styles = Styles(name=name, description=description, abvMin=abvMin, 
 # 					abvMax=abvMax, ibuMin=ibuMin, ibuMax=ibuMax,
	# 				ogMin=ogMin, ogMax=ogMax, fgMin=fgMin, fgMax=fgMax,
	# 				srmMin=srmMin, srmMax=srmMax, category=category)

	# 	db.session.add(styles)

	print "Styles"

	# db.session.commit()


def load_category():
	"""Load categories from u.category into database."""

# # r = requests.get(
# #    "http://api.brewerydb.com/v2/categories?key=391f6548d25f4637ed5fb02c80236aad&")

# # category = r.json()
# # category = category.values()
# # category = category[2]

# # for i, row in enumerate(category):
# # 	name = row['name']

# # 	category = Category(name=name)

# # 	print row['name']
# # 	# pprint(categories)


	# for i, row in enumerate(open("seed_data/u.category.txt")):
	# 	row = row.rstrip()
	# 	name = row.split("|")[1]

	# 	category = Category(name=name)

	# 	db.session.add(category)

	print "Category"

	# db.session.commit()


def load_yeast():
	"""Load yeast values from api. Then will load from a file."""

	# r = requests.get(
 #    	"http://api.brewerydb.com/v2/yeasts?key=391f6548d25f4637ed5fb02c80236aad&p=8")

	# yeast = r.json()
	# yeast = yeast.values()
	# yeast = yeast[3]

	# for i, row in enumerate(yeast):
		
	# 	if 'description' in row:
	# 		name = row['name']

	# 		if 'description' in row:
	# 			description = row['description']

	# 		if 'yeastType' in row:
	# 			yeastType = row['yeastType']
	# 		else:
	# 			yeastType = ""

	# 		if 'fermentTempMin' in row:
	# 			fermentTempMin = row['fermentTempMin']
	# 		else:
	# 			fermentTempMin = 0

	# 		if 'fermentTempMax' in row:
	# 			fermentTempMax = row['fermentTempMax']
	# 		else:
	# 			fermentTempMax = 0

	# 		if 'alcoholToleranceMin' in row:
	# 			alcoholToleranceMin = row['alcoholToleranceMin']
	# 		else:
	# 			alcoholToleranceMin = 0

	# 		if 'alcoholToleranceMax' in row:
	# 			alcoholToleranceMax = row['alcoholToleranceMax']
	# 		else:
	# 			alcoholToleranceMax = 0

	# 		if 'yeastFormat' in row:
	# 			yeastFormat = row['yeastFormat']
	# 		else:
	# 			yeastFormat = ""

	# 		yeast = Yeast(name=name, description=description, yeastType=yeastFormat, 
	# 						fermentTempMin=fermentTempMin, fermentTempMax=fermentTempMax, 
	# 						alcoholToleranceMin=alcoholToleranceMin, 
	# 						alcoholToleranceMax=alcoholToleranceMax, yeastFormat=yeastFormat)
			
	# 		db.session.add(yeast)

	# 	print "#################"

	# # pprint(yeast)

	print "Yeast"
	# db.session.commit()

def load_hops():
	"""Load hops values from api. Then will load from a file."""

	# r = requests.get(
 #    	"http://api.brewerydb.com/v2/hops?key=391f6548d25f4637ed5fb02c80236aad&p=4")

	# hops = r.json()
	# hops = hops.values()
	# hops = hops[3]

	# for i, row in enumerate(hops):
		
	# 	if 'description' in row:
	# 		name =  row['name']
	# 		if 'description' in row:
	# 			description = row['description']
	# 		else:
	# 			description = ""

	# 		if 'alphaAcidMin' in row:
	# 			alphaAcidMin = row['alphaAcidMin']
	# 		else:
	# 			alphaAcidMin = 0

	# 		if 'alphaAcidMax' in row:
	# 			alphaAcidMax = row['alphaAcidMax']
	# 		else:
	# 			alphaAcidMax = 0

	# 		if 'betaAcidMin' in row:
	# 			betaAcidMin = row['betaAcidMin']
	# 		else:
	# 			betaAcidMin = 0

	# 		if 'betaAcidMax' in row:
	# 			betaAcidMax = row['betaAcidMax']
	# 		else:
	# 			betaAcidMax = 0

	# 		if 'forBittering' in row:
	# 			print row['forBittering']
	# 		else:
	# 			print ""

	# 		if 'forFlavor' in row:
	# 			print row['forFlavor']
	# 		else:
	# 			print ""

	# 		if 'forAroma' in row:
	# 			print row['forAroma']
	# 		else:
	# 			print ""

	# 		if 'country' in row:
	# 			country = row['country']['name']
	# 		else:
	# 			country = ""

	# 		hops = Hops(name=name, description=description, alphaMin=alphaAcidMin, 
	# 						alphaMax=alphaAcidMax, betaMin=betaAcidMin, betaMax=betaAcidMax, 
	# 						originCountry=country)
	# 		db.session.add(hops)

	# 	print "############"
	# # pprint(hops)
	print "Hops"

	# db.session.commit()


def load_fermentables():
	"""Load fermentables from api. Then pull from a file."""

	r = requests.get(
    	"http://api.brewerydb.com/v2/fermentables?key=391f6548d25f4637ed5fb02c80236aad&p=5")

	fermentables = r.json()
	fermentables = fermentables.values()
	fermentables = fermentables[3]

	for i, row in enumerate(fermentables):
		if 'description' in row:
			name = row['name']

			if 'description' in row:
				description = row['description']
			else:
				description = ""

			if 'srmId' in row:
				srmId = row['srmId']
			else:
				srmId = 0

			if 'moistureContent' in row:
				moistureContent = row['moistureContent']
			else:
				moistureContent = 0

			if 'diastaticPower' in row:
				diastaticPower = row['diastaticPower']
			else:
				diastaticPower = 0

			if 'potential' in row:
				potential = row['potential']
			else:
				potential = 0

			if 'protein' in row:
				protein = row['protein']
			else:
				protein = 0

			if 'maxInBatch' in row:
				maxInBatch = row['maxInBatch']
			else:
				maxInBatch = 0

			if 'requiresMashing' in row:
				requiresMashing = row['requiresMashing']
			else:
				requiresMashing = ""

			if 'characteristics' in row:
				characteristics = row['characteristics'][0]['description']
			else:
				characteristics = ""

			if 'country' in row:
				country = row['country']['name']
			else:
				country = ""

			print "############"

			fermentables = Fermentables(name=name, description=description, srmId=srmId,
				moistureContent=moistureContent, diastaticPower=diastaticPower,
				potential=potential, protein=protein, maxInBatch=maxInBatch,
				requiresMashing=requiresMashing, characteristics=characteristics,
				country=country)

			db.session.add(fermentables)

	# pprint(fermentables)

	db.session.commit()
	print "Fermentables"



if __name__ == "__main__":
	connect_to_db(app)
	db.create_all()

	load_styles()
	load_category()
	load_yeast()
	load_hops()
	load_fermentables()
