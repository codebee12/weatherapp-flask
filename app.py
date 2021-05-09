from flask import Flask, render_template, url_for, request
import requests

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/search')
def search():
    return render_template("search.html")

@app.route('/city', methods =['POST'] )
def search_city():
    API_KEY = ''  # initialize your key here

    city = request.form['city']
   # city = request.args.get('q')  # city name passed as argument
    
    # call API and convert response into Python dictionary
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={API_KEY}'
    response = requests.get(url).json()

    # error like unknown city name, inavalid api key
    if response.get('cod') != 200:
        message = response.get('message', '')
        return f'Error getting temperature for {city.title()}. Error message = {message}'
    
    msg = response['weather'][0]['main']

    return msg

if __name__ == '__main__':
     app.run(debug=True)