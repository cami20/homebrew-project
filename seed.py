from sqlalchemy import func

import requests
from pprint import pprint


from model import Styles, Category, Yeast, Hops, Fermentables, connect_to_db, db
from server import app
import sys

reload(sys)
sys.setdefaultencoding('utf8')

def load_styles():
	"""Load styles from a seed file."""

	for i, row in enumerate(open("seed_data/styles.sql")):
		row = row.rstrip()


		styleId, name, description, abvMin, abvMax, ibuMin, ibuMax, ogMin, ogMax, fgMin, fgMax, srmMin, srmMax, category = row.split(" | ")

		styles = Styles(styleId=styleId, name=str(name), description=str(description), abvMin=str(abvMin), 
					abvMax=abvMax, ibuMin=ibuMin, ibuMax=ibuMax,
				ogMin=ogMin, ogMax=ogMax, fgMin=fgMin, fgMax=fgMax,
				srmMin=srmMin, srmMax=srmMax, category=str(category))

		db.session.add(styles)

	db.session.commit()

	print "Styles"


def load_category():
	"""Load categories from u.category into database."""

	for i, row in enumerate(open("seed_data/u.category.txt")):
		row = row.rstrip()
		name = row.split(" | ")[1]

		category = Category(name=name)

		db.session.add(category)

	print "Category"

	db.session.commit()


def load_yeast():
	"""Load yeast values from api. Then will load from a file."""

	for i, row in enumerate(open("seed_data/yeasts.sql")):
		row = row.rstrip()

		try:
			yeast_id, name, description, yeastType, fermentTempMin, fermentTempMax, alcoholToleranceMin, alcoholToleranceMax, yeastFormat = row.split("|")

			yeast = Yeast(yeast_id=yeast_id, name=name, description=description, yeastType=yeastFormat, 
						fermentTempMin=fermentTempMin, fermentTempMax=fermentTempMax, 
						alcoholToleranceMin=alcoholToleranceMin, 
						alcoholToleranceMax=alcoholToleranceMax, yeastFormat=yeastFormat)

		except ValueError:
			import pdb; pdb.set_trace()
		db.session.add(yeast)

	print "Yeast"
	db.session.commit()

def load_hops():
	"""Load hops values from api. Then will load from a file."""

	for i, row in enumerate(open("seed_data/hops.sql")):
		row = row.rstrip()

		try:
			hops_id, name, description, alphaAcidMin, alphaAcidMax, betaAcidMin, betaAcidMax, country = row.split("|")

			hops = Hops(hops_id=hops_id, name=name, description=description, alphaMin=alphaAcidMin, 
					alphaMax=alphaAcidMax, betaMin=betaAcidMin, betaMax=betaAcidMax, 
					originCountry=country)

		except ValueError:
			print i
			import pdb; pdb.set_trace()

		db.session.add(hops)

	print "Hops"

	db.session.commit()


def load_fermentables():
	"""Load fermentables from api. Then pull from a file."""

	for i, row in enumerate(open("seed_data/ferment.sql")):
		row = row.rstrip()

		try:
			fermentables_id, name, description, srmId, moistureContent, diastaticPower, potential, protein, maxInBatch, requiresMashing, characteristics, country = row.split(" | ")

			fermentables = Fermentables(fermentables_id=fermentables_id, 
				name=name, description=description, srmId=srmId, 
				moistureContent=moistureContent, diastaticPower=diastaticPower,
				potential=potential, protein=protein, maxInBatch=maxInBatch,
				requiresMashing=requiresMashing, characteristics=characteristics,
				country=country)

		except ValueError:
			print i
			import pdb; pdb.set_trace()


		db.session.add(fermentables)

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
