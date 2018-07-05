import urllib2 
import re
import requests
import sys
from bs4 import BeautifulSoup

currencySymbols = {'dollars': '$', 'rupees': 'Rs.'}

item_query = raw_input("what are you looking to buy?\n")
currency_query = raw_input("please enter your currency in words \n")

item_query = item_query.replace(" ", "+")
search_query = "https://www.google.com/search?q=" + item_query + "+price+in+" + currency_query

r = requests.get(search_query)

soup = BeautifulSoup(r.text, 'html.parser')

def extractPrice(summaryText):
	start = summaryText.find(currencySymbols[currency_query])
	if currencySymbols[currency_query] == "Rs.":
		start += 4
	else:
		start += 1
	end = summaryText.find(".", start)
	givenPrice = summaryText[start:end]

	return givenPrice


sentence = []

for g in soup.find_all(class_ = "s"):
	sentence.append(g.text)

index = -1

for i in range(len(sentence)):
	if currencySymbols[currency_query] in sentence[i]:
		index = i 
		break;

if index == -1:
	print ("I'm sorry. We could not find the price for your selected item.")
	sys.exit()

output = extractPrice(sentence[index])



print("The cost is %s%s" % (currencySymbols[currency_query], output))

