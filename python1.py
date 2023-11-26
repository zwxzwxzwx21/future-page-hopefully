
import requests
from flask import Flask, render_template
#from bs4 import BeautifulSoup
app = Flask(__name__)
key = "0c4cc278e9c7878132da2bef"
target_currency = 'PLN'
currency = "USD"

currencies = ["USD","EUR","PLN","CAD","JPY"]
price_usd = ''     
price_eur = ''
price_pln = ''
price_cad = ''
price_jpy = ''
price_currencies = [price_usd,price_eur,price_pln,price_cad,price_jpy]

'''THE CODE BELOW WORKS PERFECTLY FINE, JUST EBAY DOESNT WANNA COOPERATE BECAUSE IVE USED ALL CALLS IN API KEY AND I DONT WANNA PAY'''
#region
@app.route("/collection")
def collection():
    return render_template("collection.html")


@app.route('/')
def home():
    
    params = {
        'api_key': '0c4cc278e9c7878132da2bef',  # Replace with your actual API key
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
    price = None
    realprice = ''
    dolar = False
    apos = False

    # Check if the API call was successful
    if data['request_info']['success'] and data['search_results']:
            result = data['search_results'][0]
            image = result['image']
            title = result['title']
            link = result['link']
            price = result['prices'][0]['raw']
            for i in range(1,len(price)):
                realprice += price[i]
 #endregion   
           

    
 
    #return render_template("Mainpage.html",cur1=price_usd,cur2=price_eur,cur3=price_pln,cur4=price_cad,cur5=price_jpy, Fumo_picture=image,Fumo_link=link,Fumo_title=title,Fumo_price=realprice)
    return render_template("Mainpage.html",cur1=price_usd,cur2=price_eur,cur3=price_pln,cur4=price_cad,cur5=price_jpy)


def exchange_rates(key,target_currency):
     response = requests.get(f"http://v6.exchangerate-api.com/v6/{key}/latest/{currency}")
     if response.status_code == 200:
            data = response.json()
            
            rates = data['conversion_rates']

            usd_to_target_rate = rates[target_currency]
            return usd_to_target_rate


with app.app_context():
    
    price_eur = exchange_rates("0c4cc278e9c7878132da2bef",'EUR')
    render_template("Mainpage.html",cur1=price_eur)
    price_usd = exchange_rates("0c4cc278e9c7878132da2bef",'USD')
    render_template("Mainpage.html",cur2=price_usd)
    price_pln = exchange_rates("0c4cc278e9c7878132da2bef",'PLN')
    render_template("Mainpage.html",cur3=price_pln)
    price_cad = exchange_rates("0c4cc278e9c7878132da2bef",'CAD')
    render_template("Mainpage.html",cur4=price_cad)
    price_jpy = exchange_rates("0c4cc278e9c7878132da2bef",'JPY')
    render_template("Mainpage.html",cur5=price_jpy)





rate = exchange_rates(key,target_currency)
if rate:
     print("rate",rate)     



if __name__ == "__main__":
    app.run(debug=True)


# 1. External Links Section:
#    - Include links to important Fumo-related resources, fan sites, and official pages.
#    - Could be displayed in a sidebar or dedicated "Resources" section.

# 2. Currency Converter:
#    - Implement a currency converter for price listings.
#    - Allow users to see prices in their local currency using a currency conversion API.

# 3. Dream Fumo Collection:
#    - Create an interactive section where users can compile a list of their top 5 dream Fumo plushies.
#    - Users can mark plushies they own and save their dream list.

# 4. Community's Favorite Fumo:
#    - Develop a voting system where users can vote for their favorite Fumo plushies.
#    - Display a ranking of the top-voted Fumos.

# 5. Tutorial Videos:
#    - Embed tutorial videos on Fumo care, customization, or collecting tips.
#    - Could be sourced from YouTube or another video platform.

# 6. Fumo Gallery:
#    - Showcase a gallery of Fumo plushie pictures.
#    - Allow users to submit their own photos to the gallery. // this can be done on the featured umo collection part when you have 2 fumo pics and tou can submit your own pic and it will crop ir or something making it 3 pictures on the gallery

# 7. Pseudo-Forum:
#    - Set up a simple message board or comment section where users can discuss Fumo-related topics.
#    - Use this feature to practice backend development with databases and server-side scripting.

# 8. Fumo Plushie Spotlights:
#    - Feature detailed spotlights on different Fumo plushies, including history, variations, and fun facts.

# 9. Upcoming Releases and Events:
#    - Provide a section for news on upcoming Fumo releases and community events.

# 10. User Accounts and Profiles:
#    - Offer user account creation so users can have profiles, save their collections, and participate in the community.

# 11. Trade and Exchange Board:
#    - Create a platform for users to post and respond to trade or sale listings for Fumo plushies.

# 12. Fumo Plushie Reviews:
#    - Implement a review system where users can leave reviews for different Fumo plushies.

# 13. Customization Ideas:
#    - Share ideas and guides for customizing Fumo plushies, such as sewing accessories or creating dioramas.

# 14. Social Media Integration:
#    - Integrate with social media to allow users to share their collections or favorite plushies.

# 15. Mobile Responsiveness:
#    - Ensure the website is fully responsive so users can browse and interact with the site on mobile devices.

# 16. Guess The Fumo Quiz

# 17. watch showcase to which fumo etc