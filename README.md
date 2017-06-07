# Hoppy Home Brewer

Hoppy Home Brewer is a tool that allows users to learn more about the different styles of beer that they can make and the different ingredients that go into beer. When the user logs in or creates a new account they can make and keep track of home brew projects and make changes as they perfect their recipes. If the user needs a little inspiration in their beer planning process, they can play the Random Beer game and get a beer made of random ingredients.

## Table of Contents

* Tech Stack
* Features
* Setup/Installation
* To-Do


## Tech Stack

**Frontend:** HTML5, JavaScript, jQuery, BootStrap
**Backend:** Python, Flack, PostgreSQL, SQLAlchemy
**API:** BreweryDB


## Features
]
Search styles of beer by country of origin. User account not required.

Search hops and fermentables by country of origin. User account not required.

Search yeast by form the yeast can be bought in. User account not requried.

Play the random beer game. User account only required to save a beer.

Register or login to create new projects, view projects, and edit projects.


## Setup/Installation

### Requirements:
	* PostgreSQL
	* Python 2.7


To run this app on your local computer:

Clone repository:
	```````
	$ git clone https://github.com/cami20/homebrew-project.git
	````````

Create a virtual environment:
	$ virtualenv env

Activate the virtual environment:
	$ source env/bin/activate

Install dependencies:
	$ pip install -r requirements.txt

Create database 'homebrew':
	$ createdb homebrew

Create your database tables and seed the database:
	$ python seed.py

Run the app from the command line.
	$ python server.py


##Todo:

* create links between ingredients and projects.
* refactor
