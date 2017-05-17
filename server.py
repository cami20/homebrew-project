"""Homebrew project server"""

from jinja2 import StrictUndefined

from flask import Flask, render_template, request, flash, redirect, session
from flask_debugtoolbar import DebugToolbarExtension
from model import connect_to_db, db, Styles, Yeast, Hops, Fermentables, User

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
	"""Displays the styles landing page."""

	styles = Styles.query.all()
	return render_template('styles.html', styles=styles)

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
	# user = User.query.filter_by(email=username | username=username).first()

	# if not user:
	# 	flash("Your information is not in our records. Please try again.")
	# 	return redirect("/login")

	# if user.password != password:
	# 	flash("Incorrect password")
	# 	return redirect("/login")

	# session["user_id"] = user.user_id

	flash("Logged in")
	return redirect("/")

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

	# use the code below to add users to the database.
	new_user = User(email=email, username=username, password=password)

	db.session.add(new_user)
	db.session.commit()

	flash("User %s added." % email)
	return redirect("/")

@app.route('/yeast')
def yeast_info():
	"""Displays info about yeast."""

	yeasts = Yeast.query.all()
	return render_template('yest.html', yeasts=yeasts)

@app.route('/yeast-display/<name>')
def yeast_display(name):
	"""Displays the specific info about a yeast."""

	yeast = Yeast.query.filter_by(name=name).first()
	return render_template('yeast_display.html', yeast=yeast)

@app.route('/hops')
def hops_info():
	"""Displays info about hops."""

	hops = Hops.query.all()
	return render_template('hops.html', hops=hops)

@app.route('/hops-display/<name>')
def hops_display(name):
	"""Displays the specific info about a hop."""

	hops = Hops.query.filter_by(name=name).first()
	return render_template('hops_display.html', hops=hops)

@app.route('/fermentables')
def fermentables_info():
	"""Displays info about fermentables."""

	fermentables = Fermentables.query.all()
	return render_template('ferment.html', fermentables=fermentables)

@app.route('/fermentable-display/<name>', methods=["GET"])
def fermentable_display(name):
	"""Displays the specific info about a fermentable."""

	fermentables = Fermentables.query.filter_by(name=name).first()
	return render_template('ferment_display.html', fermentables=fermentables)

@app.route('/random')
def display_random():
	"""Displays the random ingredients game."""

	return render_template('random_beer.html')

@app.route('/profile')
def display_profile():
	"""Displays a users profile"""

	return render_template('profile.html')


if __name__ == "__main__":
    app.debug = True

    connect_to_db(app)

    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")