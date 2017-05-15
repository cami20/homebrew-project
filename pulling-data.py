import requests
from pprint import pprint

#this is a basic way of importing my data from the api
#I will currently write code for all the things I want to pull in then
#will need to find a better way to pull it in so I can format it.

#hops

# r = requests.get(
#     "http://api.brewerydb.com/v2/hops?key=391f6548d25f4637ed5fb02c80236aad&p=1")
# r2 = requests.get(
#     "http://api.brewerydb.com/v2/hops?key=391f6548d25f4637ed5fb02c80236aad&p=2")
# r3 = requests.get(
#     "http://api.brewerydb.com/v2/hops?key=391f6548d25f4637ed5fb02c80236aad&p=3")
# r4 = requests.get(
#     "http://api.brewerydb.com/v2/hops?key=391f6548d25f4637ed5fb02c80236aad&p=4")


# hops = r.json()
# hops2 = r2.json()
# hops3 = r3.json()
# hops4 = r4.json()



# pprint(hops)
# pprint(hops2)
# pprint(hops3)
# pprint(hops4)

#yeast

# r = requests.get(
#     "http://api.brewerydb.com/v2/yeasts?key=391f6548d25f4637ed5fb02c80236aad&p=1")
# r2 = requests.get(
#     "http://api.brewerydb.com/v2/yeasts?key=391f6548d25f4637ed5fb02c80236aad&p=2")
# r3 = requests.get(
#     "http://api.brewerydb.com/v2/yeasts?key=391f6548d25f4637ed5fb02c80236aad&p=3")
# r4 = requests.get(
#     "http://api.brewerydb.com/v2/yeasts?key=391f6548d25f4637ed5fb02c80236aad&p=4")
# r5 = requests.get(
#     "http://api.brewerydb.com/v2/yeasts?key=391f6548d25f4637ed5fb02c80236aad&p=5")
# r6 = requests.get(
#     "http://api.brewerydb.com/v2/yeasts?key=391f6548d25f4637ed5fb02c80236aad&p=6")
# r7 = requests.get(
#     "http://api.brewerydb.com/v2/yeasts?key=391f6548d25f4637ed5fb02c80236aad&p=7")
# r8 = requests.get(
#     "http://api.brewerydb.com/v2/yeasts?key=391f6548d25f4637ed5fb02c80236aad&p=8")

# yeast = r.json()
# yeast2 = r2.json()
# yeast3 = r3.json()
# yeast4 = r4.json()
# yeast5 = r5.json()
# yeast6 = r6.json()
# yeast7 = r7.json()
# yeast8 = r8.json()



# pprint(yeast)
# pprint(yeast2)
# pprint(yeast3)
# pprint(yeast4)
# pprint(yeast5)
# pprint(yeast6)
# pprint(yeast7)
# pprint(yeast8)


#fermentables

r = requests.get(
    "http://api.brewerydb.com/v2/fermentables?key=391f6548d25f4637ed5fb02c80236aad&p=1")
# r2 = requests.get(
#     "http://api.brewerydb.com/v2/fermentables?key=391f6548d25f4637ed5fb02c80236aad&p=2")
# r3 = requests.get(
#     "http://api.brewerydb.com/v2/fermentables?key=391f6548d25f4637ed5fb02c80236aad&p=3")
# r4 = requests.get(
#     "http://api.brewerydb.com/v2/fermentables?key=391f6548d25f4637ed5fb02c80236aad&p=4")
# r5 = requests.get(
#     "http://api.brewerydb.com/v2/fermentables?key=391f6548d25f4637ed5fb02c80236aad&p=5")

fermentables = r.json()
# fermentables2 = r2.json()
# fermentables3 = r3.json()
# fermentables4 = r4.json()
# fermentables5 = r5.json()



pprint(fermentables)
# pprint(fermentables2)
# pprint(fermentables3)
# pprint(fermentables4)
# pprint(fermentables5)


# styles

r = requests.get(
    "http://api.brewerydb.com/v2/styles?key=391f6548d25f4637ed5fb02c80236aad&")

styles = r.json()

pprint(styles)


#categories
#now I have a seed file for this!!!!

# r = requests.get(
#     "http://api.brewerydb.com/v2/categories?key=391f6548d25f4637ed5fb02c80236aad&")

# categories = r.json()

# pprint(categories)

