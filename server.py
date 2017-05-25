"""Homebrew project server"""

from jinja2 import StrictUndefined

from flask import Flask, render_template, request, flash, redirect, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from model import connect_to_db, db, Styles, Yeast, Hops, Fermentables, User , Project

import random

app = Flask(__name__)

app.secret_key = "shhSecretshh"

app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
	"""Homepage"""

	return render_template('homepage.html')

@app.route('/ingredients')
def ingredients():
	"""Displays the ingredients landing page"""

	return render_template('ingredients.html')

@app.route('/styles')
def styles():
	"""Displays the all styles."""

	return render_template('styles.html')

@app.route('/styles.json')
def display_styles():
	"""Searches styles by category then displays the narrowed down data."""

	display_styles = []
	cat = request.args.get('cat')

	if cat == "all":
		styles = Styles.query.all()
	else:
		styles = Styles.query.filter(Styles.category==cat).all()

	for style in styles:
		display_styles.append(style.name)
		# print display_styles
	return jsonify(display_styles)

@app.route('/style-display/<name>')
def style_display(name):
	"""Will display the selected style's information."""

	styles = Styles.query.filter_by(name=name).first()
	return render_template('styles_display.html', styles=styles)

@app.route('/login')
def login():
	"""Show the login form."""

	return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_process():
	"""Process login."""

	username = request.form["username"]
	password = request.form["password"]

	# use the code below to validate users and log them into their accounts
	user = User.query.filter((User.email==username) | (User.username==username)).first()

	if not user:
		flash("Your information is not in our records. Please try again.")
		return redirect("/login")

	if user.password != password:
		flash("Incorrect password")
		return redirect("/login")

	session["username"] = user.username
	print "Login check", session['username']

	flash("Logged in")
	return redirect("/")

@app.route('/logout')
def logout():
	"""Logs the user out by deleting the session."""

	del session['username']
	flash('Logged out.')
	print "Log out check", session.get('username')
	return redirect('/')

@app.route('/new-account', methods=['GET'])
def new_account():
	"""Show form for user signup."""

	return render_template('new_account.html')

@app.route('/new-account', methods=['POST'])
def new_account_process():
	"""Process the registration."""

	#Get form variables
	email = request.form["email"]
	username = request.form["username"]
	password = request.form["password"]

	if User.query.filter((User.email==email) | (User.username==username)).first():
		# print "check user in database", User.query.filter((User.email==email) | (User.username==username)).all()
		flash("%s you already have an accout. Please sign in." % username)
		return redirect("/login")

	# use the code below to add users to the database.
	new_user = User(email=email, username=username, password=password)

	db.session.add(new_user)
	db.session.commit()

	flash("User %s added." % email)
	session["username"] = new_user.username
	return redirect("/")

	#TODO: make it so there can't be dublicate accounts

@app.route('/yeast')
def yeast_info():
	"""Displays info about yeast."""

	return render_template('yest.html')

@app.route('/yeasts.json')
def display_yeasts():
	"""Searches yeasts by form you can by them in then displays the narrowed down data."""

	display_yeasts = []
	yf = request.args.get('yf')

	if yf == "all":
		yeasts = Yeast.query.all()
	else:
		yeasts = Yeast.query.filter(Yeast.yeast_format==yf).all()

	for yeast in yeasts:
		display_yeasts.append(yeast.name)
		# print display_styles
	return jsonify(display_yeasts)

@app.route('/yeast-display/<name>')
def yeast_display(name):
	"""Displays the specific info about a yeast."""

	yeast = Yeast.query.filter_by(name=name).first()
	return render_template('yeast_display.html', yeast=yeast)

@app.route('/hops')
def hops_info():
	"""Displays info about hops."""

	return render_template('hops.html')

@app.route('/hops.json')
def display_hops():
	"""Searches hops by country of origin then displays the narrowed down data."""

	display_hops = []
	coo = request.args.get('coo')

	if coo == "all":
		hops = Hops.query.all()
	else:
		hops = Hops.query.filter(Hops.origin_country==coo).all()

	for hop in hops:
		display_hops.append(hop.name)
		# print display_styles
	return jsonify(display_hops)

@app.route('/hops-display/<name>')
def hops_display(name):
	"""Displays the specific info about a hop."""

	hops = Hops.query.filter_by(name=name).first()
	return render_template('hops_display.html', hops=hops)

@app.route('/fermentables')
def fermentables_info():
	"""Displays info about fermentables."""

	return render_template('ferment.html')

@app.route('/fermentables.json')
def display_fermentables():
	"""Searches fermentables by country of origin then displays the narrowed down data."""

	display_fermentables = []
	fcoo = request.args.get('fcoo')

	if fcoo == "all":
		fermentables = Fermentables.query.all()
	else:
		fermentables = Fermentables.query.filter(Fermentables.country==fcoo).all()

	for fermentable in fermentables:
		display_fermentables.append(fermentable.name)
		# print display_styles
	return jsonify(display_fermentables)

@app.route('/fermentable-display/<name>', methods=["GET"])
def fermentable_display(name):
	"""Displays the specific info about a fermentable."""

	fermentables = Fermentables.query.filter_by(name=name).first()
	return render_template('ferment_display.html', fermentables=fermentables)

@app.route('/profile')
def display_profile():
	"""Displays a users profile"""

	#find a way to display empty profile if session is active
	#or only display profile if you have a session active and hide profile
	#if you are not signed in 
	# return render_template('profile.html')

	name = session['username']
	display = User.query.filter(User.username==name).all()

	if not display:
		flash('Please log in to create a new project')
	elif display:
		projects = Project.query.filter(Project.username==name).all()
		return render_template('profile.html', projects=projects)
	else:
		flash('Please log in or create a new account to view projects.')
		return render_template('profile.html')
		
@app.route('/project-display/<name>', methods=['GET'])
def display_project(name):
	"""Display the info about a specific project"""

	projects = Project.query.filter_by(project_name=name).first()
	return render_template('project_display.html', projects=projects)

@app.route('/new-project')
def display_new_project():
	"""Displays the new project form."""
	#make text box for notes bigger in the CSS file
	return render_template('new-project-form.html')

@app.route('/project.json')
def edit_project():

	display_project = []

	name = request.args.get('name')

	info = Project.query.filter_by(project_name=name).first()

	display_project = {"name": info.project_name, "style": info.style, "yeast": info.yeast, 
						"hops": info.hops, "hops2": info.hops2, "hops3": info.hops3, 
						"fermentables": info.fermentables, "fermentables2": info.fermentables2, 
						"fermentables3": info.fermentables3, "og": info.og, "fg": info.fg, 
						"abv": info.abv, "srm": info.srm, "notes": info.notes}

	return jsonify(display_project)

@app.route('/edit-project/<name>', methods=['GET'])
def display_edit_project(name):

	projects = Project.query.filter_by(project_name=name).first()
	return render_template("edit-project.html", projects=projects)

@app.route('/edit-project', methods=['POST'])
def edit_project_process():
	"""Process of editing a project."""

	# Get form variables
	username = session['username']
	name = request.form['project_name']
	style = request.form['style']
	yeast = request.form['yeast']
	hops = request.form['hops']
	hops2 = request.form['hops2']
	hops3 = request.form['hops3']
	fermentables = request.form['fermentables']
	fermentables2 = request.form['fermentables2']
	fermentables3 = request.form['fermentables3']
	og = request.form['og']
	fg = request.form['fg']
	abv = request.form['abv']
	srm = request.form['srm']
	notes = request.form['notes']

	#use the code below to add projects to the database.
	update_project = Project(username=username, project_name=name, style=style, 
						yeast=yeast,hops=hops, hops2=hops2, hops3=hops3, 
						fermentables=fermentables,fermentables2=fermentables2, 
						fermentables3=fermentables3,og=og, fg=fg, abv=abv, 
						srm=srm, notes=notes)

	db.session.add(update_project)
	db.session.commit()

	flash("Project Updated!")
	return redirect('/profile')

@app.route('/new-project', methods=['POST'])
def new_project_process():
	"""Process of adding a new project."""

	# Get form variables
	username = session['username']
	name = request.form['project_name']
	style = request.form['style']
	yeast = request.form['yeast']
	hops = request.form['hops']
	hops2 = request.form['hops2']
	hops3 = request.form['hops3']
	fermentables = request.form['fermentables']
	fermentables2 = request.form['fermentables2']
	fermentables3 = request.form['fermentables3']
	og = request.form['og']
	fg = request.form['fg']
	abv = request.form['abv']
	srm = request.form['srm']
	notes = request.form['notes']

	#use the code below to add projects to the database.
	new_project = Project(username=username, project_name=name, style=style, 
						yeast=yeast,hops=hops, hops2=hops2, hops3=hops3, 
						fermentables=fermentables,fermentables2=fermentables2, 
						fermentables3=fermentables3,og=og, fg=fg, abv=abv, 
						srm=srm, notes=notes)

	db.session.add(new_project)
	db.session.commit()

	flash("New Project Created")
	return redirect('/profile')

@app.route('/random-beer')
def random_beer():
	"""Shows the button to select the random beer"""

	return render_template('random_beer.html')

@app.route('/random-beer-display')
def display_random_beer():
	"""Displays the random ingredients choosen."""

	hops_random = random.randint(1, 83)
	hops = Hops.query.filter_by(hops_id=hops_random).first()

	hops_random2 = random.randint(0, 83)

	if hops_random2 == 0:
		hops2 = "None"
	hops2 = Hops.query.filter_by(hops_id=hops_random2).first()

	hops_random3 = random.randint(0, 83)
	if hops_random3 == 0:
		hops3 = "None"
	hops3 = Hops.query.filter_by(hops_id=hops_random3).first()

	yeast_random = random.randint(1, 132)
	yeast = Yeast.query.filter_by(yeast_id=yeast_random).first()

	ferment_random = random.randint(1, 51)
	fermentables = Fermentables.query.filter_by(fermentables_id=ferment_random).first()

	ferment_random2 = random.randint(0, 51)
	if ferment_random2 == 0:
		fermentables2 = "None"
	fermentables2 = Fermentables.query.filter_by(fermentables_id=ferment_random2).first()

	ferment_random3 = random.randint(0, 51)
	if ferment_random2 == 0:
		fermentables3 = "None"
	fermentables3 = Fermentables.query.filter_by(fermentables_id=ferment_random3).first()

	return render_template('random_beer_display.html', hops=hops, hops2=hops2, 
							hops3=hops3, yeast=yeast, fermentables=fermentables, 
							fermentables2=fermentables2, fermentables3=fermentables3)



if __name__ == "__main__":
    app.debug = True

    connect_to_db(app)

    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")