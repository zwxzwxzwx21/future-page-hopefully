import requests
import json

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

# print the JSON response from Countdown API
'''print(json.dumps(api_result.json()))'''
data = api_result.json()
track = 0

for item in data['search_results']:
        while track == 0:
            title = item['title']
            link = item['link']
            image = item['image']

            print(len(data['search_results']))
            print(title)
            print(link)
            print(image)
            print("----------")
            track += 1
            if track >0:
                  break