'''import requests
import json
from flask import Flask, render_template
app = Flask(__name__) 

@app.route('/')
def home():
  # set up the request parameters
  params = {
  'api_key': '803AD7F6083349A785387A19D385DD14',
    'ebay_domain': 'ebay.com',
    'search_term': 'fumo plush',
    'type': 'search',
    'page': '1',
    'max_page': '1',
    'sort_by': 'newly_listed',
    'output': 'json',
    'include_html': 'true'
  }

  # make the http GET request to Countdown API
  api_result = requests.get('https://api.countdownapi.com/request', params)

 
  
  data = api_result.json()
  track = 0
  image = None
  if data["search_results"]:
       image = data['search_results'][0]['image']
  

            

  #Fumo_picture = image
  return render_template("Mainpage.html",Fumo_picture=image)
  if __name__ == '__main__':
      app.run(debug=True)

'''

import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Set up the request parameters
    params = {
        'api_key': '803AD7F6083349A785387A19D385DD14',  # Replace with your actual API key
        'ebay_domain': 'ebay.com',
        'search_term': 'fumo plush',
        'type': 'search',
        'page': '1',
        'max_page': '1',
        'sort_by': 'newly_listed',
        'output': 'json',
        'include_html': 'true'
    }

    # Make the http GET request to Countdown API
    api_result = requests.get('https://api.countdownapi.com/request', params)
    data = api_result.json()

    # Initialize the image variable
    image = None
    title = None
    link = None

    # Check if the API call was successful
    if data['request_info']['success'] and data['search_results']:
            result = data['search_results'][0]
            image = result['image']
            title = result['title']
            link = result['link']
    
 
    return render_template("Mainpage.html", Fumo_picture=image,Fumo_link=link,Fumo_title=title)
    

# Make sure this is at the bottom of your script
if __name__ == '__main__':
    app.run(debug=True)
