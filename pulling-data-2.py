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


# 	# r = requests.get(
#  #    	"http://api.brewerydb.com/v2/yeasts?key=391f6548d25f4637ed5fb02c80236aad&p=8")

# 	# yeast = r.json()
# 	# yeast = yeast.values()
# 	# yeast = yeast[3]

# 	# for i, row in enumerate(yeast):
		
# 	# 	if 'description' in row:
# 	# 		name = row['name']

# 	# 		if 'description' in row:
# 	# 			description = row['description']

# 	# 		if 'yeastType' in row:
# 	# 			yeastType = row['yeastType']
# 	# 		else:
# 	# 			yeastType = ""

# 	# 		if 'fermentTempMin' in row:
# 	# 			fermentTempMin = row['fermentTempMin']
# 	# 		else:
# 	# 			fermentTempMin = 0

# 	# 		if 'fermentTempMax' in row:
# 	# 			fermentTempMax = row['fermentTempMax']
# 	# 		else:
# 	# 			fermentTempMax = 0

# 	# 		if 'alcoholToleranceMin' in row:
# 	# 			alcoholToleranceMin = row['alcoholToleranceMin']
# 	# 		else:
# 	# 			alcoholToleranceMin = 0

# 	# 		if 'alcoholToleranceMax' in row:
# 	# 			alcoholToleranceMax = row['alcoholToleranceMax']
# 	# 		else:
# 	# 			alcoholToleranceMax = 0

# 	# 		if 'yeastFormat' in row:
# 	# 			yeastFormat = row['yeastFormat']
# 	# 		else:
# 	# 			yeastFormat = ""

# 	# 		yeast = Yeast(name=name, description=description, yeastType=yeastFormat, 
# 	# 						fermentTempMin=fermentTempMin, fermentTempMax=fermentTempMax, 
# 	# 						alcoholToleranceMin=alcoholToleranceMin, 
# 	# 						alcoholToleranceMax=alcoholToleranceMax, yeastFormat=yeastFormat)
			
# 	# 		db.session.add(yeast)

# 	# 	print "#################"






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



# 	# r = requests.get(
#  #    	"http://api.brewerydb.com/v2/fermentables?key=391f6548d25f4637ed5fb02c80236aad&p=5")

# 	# fermentables = r.json()
# 	# fermentables = fermentables.values()
# 	# fermentables = fermentables[3]

# 	# for i, row in enumerate(fermentables):
# 	# 	if 'description' in row:
# 	# 		name = row['name']

# 	# 		if 'description' in row:
# 	# 			description = row['description']
# 	# 		else:
# 	# 			description = ""

# 	# 		if 'srmId' in row:
# 	# 			srmId = row['srmId']
# 	# 		else:
# 	# 			srmId = 0

# 	# 		if 'moistureContent' in row:
# 	# 			moistureContent = row['moistureContent']
# 	# 		else:
# 	# 			moistureContent = 0

# 	# 		if 'diastaticPower' in row:
# 	# 			diastaticPower = row['diastaticPower']
# 	# 		else:
# 	# 			diastaticPower = 0

# 	# 		if 'potential' in row:
# 	# 			potential = row['potential']
# 	# 		else:
# 	# 			potential = 0

# 	# 		if 'protein' in row:
# 	# 			protein = row['protein']
# 	# 		else:
# 	# 			protein = 0

# 	# 		if 'maxInBatch' in row:
# 	# 			maxInBatch = row['maxInBatch']
# 	# 		else:
# 	# 			maxInBatch = 0

# 	# 		if 'requiresMashing' in row:
# 	# 			requiresMashing = row['requiresMashing']
# 	# 		else:
# 	# 			requiresMashing = ""

# 	# 		if 'characteristics' in row:
# 	# 			characteristics = row['characteristics'][0]['description']
# 	# 		else:
# 	# 			characteristics = ""

# 	# 		if 'country' in row:
# 	# 			country = row['country']['name']
# 	# 		else:
# 	# 			country = ""

# 	# 		print "############"

# 	# 		fermentables = Fermentables(name=name, description=description, srmId=srmId,
# 	# 			moistureContent=moistureContent, diastaticPower=diastaticPower,
# 	# 			potential=potential, protein=protein, maxInBatch=maxInBatch,
# 	# 			requiresMashing=requiresMashing, characteristics=characteristics,
# 	# 			country=country)

# 	# 		db.session.add(fermentables)

# 	# # pprint(fermentables)


#a way I found to save data between pages using JSON and JavaScript

 # // var val = result;
# 		// sessionStorage.setItem('val', JSON.stringify(val));
# 		// sessionStorage.val = JSON.stringify(val);
# 		// console.log(val);
# 		// $.each(result, function(key, value){
# 		// 	var update = $('[name=' +key+']', frm);
# 		// 	switch(update.prop("type"))
# 		// });

