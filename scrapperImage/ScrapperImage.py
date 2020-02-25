from bs4 import Beautifulsoup
import os
import json
import urllib.request
import urllib.parse
import urllib.error
from urllib.request import urlretrieve


class ScrapperImage:

	# creating image url
	def createImageUrl(searchterm):
		searchterm = searchterm.split() # splitting search term on spaces (ex: "Brad Pitt")
		searchterm = "+".join(searchterm) # ex: Brad+Pitt (that's how google url requires it to be)
		web_url = "https://www.google.com/search?q=" + searchterm + "&source=lnms&tbm=isch"
		return web_url

	# get raw html
	def scrape_html_data(url, header):
		request = urllib.request.Request(url, headers=header)
		response = urllib.request.urlopen(request)
		response_data = response.read()
		html = Beautifulsoup(response_data, "html.parser")
		return html

