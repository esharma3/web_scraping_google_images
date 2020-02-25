from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def home():
	print("Welcome to Google Image Web Scraping")
	return render_template("index.html")

@app.route("/showImages")
# def displayImages():
#     list_images=os.listdir('static')
#     print(list_images)
    
#     try:
#         if (len(list_images)>0):
#             return render_template('showImages.html',user_images=list_images)
#         else:
#             return "Images are not present"
#     except Exception as e:
#         print("No images found",e)
#         return "Please try with a different search keyword"
def images():
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


# ---- main -----/

if __name__ == "__main__":
	app.run(debug=True)