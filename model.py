"""Models and database functions for Homew Brew project"""

from flask_sqlalchemy import SQLAlchemy
#import correlation

db = SQLAlchemy()


class Styles(db.Model):
	"""Styles of beer that can be made"""

	__tablename__ = "styles"

	styleId = db.Column(db.Integer, autoincrement=True, primary_key=True)
	name = db.Column(db.String(65), nullable=False)
	description = db.Column(db.String(2950))
	abvMin = db.Column(db.Float)
	abvMax = db.Column(db.Float)
	ibuMin = db.Column(db.Float)
	ibuMax = db.Column(db.Float)
	ogMin = db.Column(db.Float)
	ogMax = db.Column(db.Float)
	fgMin = db.Column(db.Float)
	fgMax = db.Column(db.Float)
	srmMin = db.Column(db.Float)
	srmMax = db.Column(db.Float)
	category = db.Column(db.String(35)) #, db.ForeignKey('category.name'))

	def __repr__(self):
		"""Provides basic info when printed"""

		return "Styles name= %s, category= %s, id=%d" % (self.name, self.category, self.styleId)


class Category(db.Model):
	"""Category that a style could be under."""

	__tablename__ = "category"

	category_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	name = db.Column(db.String(35), unique=True)

	# style = db.relationship("Style",
	# 						backref=db.backref("category", order_by=name))

	def __repr__(self):
		"""Provides some info."""

		return "Name = %s" % (self.name)


class Yeast(db.Model):
	"""Types of yeast that could be used in beer making."""

	__tablename__ = "yeasts"

	yeast_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	name = db.Column(db.String(30), nullable=False)
	description = db.Column(db.String(800), nullable=False)
	yeastType = db.Column(db.String(15))
	fermentTempMin = db.Column(db.Float)
	fermentTempMax = db.Column(db.Float)
	alcoholToleranceMin = db.Column(db.Float)
	alcoholToleranceMax = db.Column(db.Float)
	yeastFormat = db.Column(db.String(10))
		# db.ForeignKey('yeast_form.form_found'))

	# def __repr__(self):
	# 	"""Provides basic info when printed"""

	# 	return "Yeast name= %s, form found in= %s" % (self.name, self.yeastFormat)


# class YeastForm(db.Model):
# 	"""The forms yeast can be purchased in."""

# 	__tablename__ = "yeast_form"

# 	form_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
# 	form_found = db.Column(db.String(10), db.ForeignKey('yeasts.form_found'))

# 	found = db.relationship("Yeast",
# 							backref=db.backref("yeast_form", order_by=form_found))


class Hops(db.Model):
	"""Types of hops that could be used in beer making."""

	__tablename__ = "hops"

	name = db.Column(db.String(35), primary_key=True, nullable=False)
	description = db.Column(db.String(1400), nullable=False)
	alphaMin = db.Column(db.Float)
	alphaMax = db.Column(db.Float)
	betaMin = db.Column(db.Float)
	betaMax = db.Column(db.Float)
	# typical_use = db.Column(db.String(10), db.ForeignKey('hop_use.typical_use'))
	originCountry = db.Column(db.String(20))

	def __repr__(self):
		"""Provides basic info when printed"""

		return "Hops name= %s" % (self.name) #, , typpically used for= %s self.typical_use)


# class HopUse(db.Model):
# 	"""The typical way a hop is used"""

# 	__tablename__ = "hop_use"

# 	use_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
# 	typical_use = db.Column(db.String(10), db.ForeignKey('hops.typical_use'))

# 	use = db.relationship("Hops",
# 							backref=db.backref("hop_use", order_by=typical_use))


# class ProjectHop(db.Model):
# 	"""The way a hop is used in a project."""

# 	__tablename__ = "project_hop"

# 	ph_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
# 	hop_name = db.Column(db.String(24), db.ForeignKey('hops.hop_id'))
# 	project_id = db.Column(db.Integer, db.ForeignKey('projects.project_id'))

# 	hop = db.relationship("Hops",
# 							backref=db.backref("ProjectHop", order_by=hop_name))

# 	projects = db.relationship("Projects",
# 								backref=db.backref("ProjectHop", order_by=project_id))


class Fermentables(db.Model):
	"""Types of fermentables that could be used in beer making."""

	__tablename__ = "fermentables"

	name = db.Column(db.String(35), primary_key=True, nullable=False)
	description = db.Column(db.String(450), nullable=False)
	srmId = db.Column(db.Float)
	moistureContent = db.Column(db.Float)
	diastaticPower = db.Column(db.Float)
	potential = db.Column(db.Float)
	protein = db.Column(db.Float)
	maxInBatch = db.Column(db.Float)
	requiresMashing = db.Column(db.String(10))
	characteristics = db.Column(db.String(200))
	country = db.Column(db.String(15))

	# def __repr__(self):
		# """Provides basic info when printed."""

		#original repr
		#return "Fermentable name= %s" % (self.name)
		# return "name: %s\n description: %s\n SRM: %s\n Moisture Content: %s\n Country: %s\n" % (self.name, self.description, self.srmId, self.moistureContent, self.country)


# class ProjectFerment(db.Model):
# 	"""Keeps track of the fermentables in each project."""

# 	__tablename__ = "project_ferment"

# 	pf_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
# 	ferment_name = db.Column(db.Integer, db.ForeignKey('fermentables.ferment_id'))
# 	project_id = db.Column(db.Integer, db.ForeignKey('projects.project_id'))

# 	fermentables = db.relationship("Fermentables",
# 									backref=db.backref("ProjectFerment", 
# 									order_by=ferment_name))

# 	projects = db.relationship("Projects",
# 								backref=db.backref("ProjectFerment", order_by=project_id))


class User(db.Model):
	"""User of the website."""

	__tablename__ = "users"

	username = db.Column(db.String(20), primary_key=True, nullable=False, unique=True)
	password = db.Column(db.String(20), nullable=False)
	email = db.Column(db.String(50), nullable=False)

	def __repr__(self):
		"""Proviedes basic info when printed"""

		return "username= %s, email= %s" % (self.username, self.email)


# class Project(db.Model):
# 	"""Projects stored in the website."""

# 	__tablename__ = "projects"

# 	project_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
# 	username = db.Column(db.String(20), db.ForeignKey('users.username'))
# 	project_name = db.Column(db.String(20))
# 	style = db.Column(db.String(20))
# 	yeast = db.Column(db.String(20))
# 	hops = db.Column(db.String(20), nullable=False)
# 	hops2 = db.Column(db.String(20))
# 	hops3 = db.Column(db.String(20))
# 	fermentables = db.Column(db.String(20), nullable=False)
# 	fermentables2 = db.Column(db.String(20))
# 	fermentables3 = db.Column(db.String(20))
# 	og = db.Column(db.Decimal)
# 	fg = db.Column(db.Decimal)
# 	abv = db.Column(db.Decimal)
# 	srm = db.Column(db.Decimal)
# 	notes = db.Column(db.Text)

# 	user = db.relationship("User", 
# 							backref=db.backref("projects", order_by=username))

# 	hops = db.relationship("Hops",
# 							secondary="project_hop"
# 							backref=db.backref"projects", order_by=hops)

# 	fermentables = db.relationship("Fermentables",
# 							secondary="project_ferment"
# 							backref=db.backref"projects", order_by=fermentables)

# 	def __repr__(self):
# 		"""Provides some basic info when printed"""

# 		return "project= %s, user= %s" % (self.project_id, self.user_id)


def connect_to_db(app):
	"""Connects the database to the Flask app."""

	#configure the PostgreSQL database
	app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///homebrew'
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
	db.app = app
	db.init_app(app)


if __name__ == "__main__":
	from server import app
	connect_to_db(app)
	print "Connected to DB."
