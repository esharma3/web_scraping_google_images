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
		html = response.read()
		soup = Beautifulsoup(response_data, "html.parser")
		return soup

	# extracting image link and ext
	def get_img_url_list(soup):
		img_url_list = []

		for item in soup.find_all("div", class_="rg_meta"):
			link = json.loads(item.text)["ou"]
			ext = json.loads(item.text)["ity"]
			img_url_list.append((link, ext))

		print(f"There are total {len(img_url_list)} images.")
		return img_url_list


	def download_images(img_url_list, img_name, header):
		master_img_list = []
		img_files = []
		img_types = []
		count = 0
		img_counter = 0

		for i, (link, type) in enumerate(img_url_list):

			try:
				if count > 10:
					break
				else:
					count += 1
					req = urllib.request.Request(link, headers=header)
					try:
						urllib.request.urlretrieve(link, "./static/" + img_name + str(img_counter) + ".jfif")
						img_counter += 1
					except Exception as e:
						print("Download Failed ", e)
						img_counter += 1

					response = urllib.request.urlopen(req)
					raw_img = response.read()

					img_files.append(raw_img)
					img_types.append(type)

			except Exception as e:
				print("Failed to download ", link)
				print(e)
				count += 1

		master_img_list.append(img_files)
		master_img_list.append(img_types)

		return img_list


		def delete_downloaded_images(self, list_of_images):
			for self.image in list_of_images:
				try:
					os.remove("./static"+self.image)
				except Exception as e:
					print("Error in deleting ", e)
			return 0














