from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route("/")
def home():
	print("Welcome to Google Image Web Scraping")
	return render_template("index.html")

@app.route("/showImages")
def displayImages():
	list_images = os.listdir("static")
	print(list_images)

	try:
		if (len(list_images) > 0):
			return render_template("showImages.html", user_images=list_images)
		else:
			return "No Images Found"

	except exception as e:
		print("Images not found", e)
		return "Please try a different search keyword"


@app.route("/searchImages", methods="POST")
def searchImage():
	if request.method == "POST";  # when the user clicks on the 'submit' button
		search_keyword = request.form["keyword"]  # from the form (in index.html)
	else:
		print("Enter the search keyword")




# ---- main -----/

if __name__ == "__main__":
	app.run(debug=True)