from scrapperImage.ScrapperImage import ScrapperImage

class BusinessLayer:

	keyword = ""
	fileLoc = ""
	image_name = ""
	header = ""

	def downloadImages(keyword, header):

		imgScrapper = ScrapperImage  # creating an object of ScarpperImage class (data layer)
		url = imgScrapper.createImageUrl(keyword)
		rawHtml = imgScrapper.scrape_html_data(url, header)