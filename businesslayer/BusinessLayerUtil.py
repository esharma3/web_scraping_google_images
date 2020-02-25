from scrapperImage.ScrapperImage import ScrapperImage

class BusinessLayer:

	keyword = ""
	fileLoc = ""
	image_name = ""
	header = ""

	def downloadImages(keyword, header):

		imgScrapper = ScrapperImage  # creating an object of ScarpperImage class (data layer)
		url = imgScrapper.createImageUrl(keyword)
		soup = imgScrapper.scrape_html_data(url, header)

		img_url_list = imgScrapper.get_img_url_list(soup)

		img_list = imgScrapper.download_images(img_url_list, keyword, header)

		return img_list