from flask import Flask, render_template, jsonify
import requests
import random

app = Flask(__name__, template_folder='templates')
app.config["EXPLAIN_TEMPLATE_LOADING"] = True

API_KEY="" # Add you API Key

NASA_ENDPOINT="https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/fetch_mars_rover_images')
def fetch_images():
    try:
        # Make API call to NASA API to fetch images
        response = requests.get(NASA_ENDPOINT, params={"api_key": API_KEY})
        data = response.json()

        # Extract image URLs from API response
        image_urls = [item["img_src"] for item in data["photos"]]

        return render_template('index.html', image_urls=image_urls)
    except Exception as e:
        return jsonify(error=str(e))
