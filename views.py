from flask import Blueprint, render_template
from flask import request
import requests
import os
#from dotenv import load_dotenv
#load_dotenv()

# Create a blueprint
main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    error_message = None
    
    if request.method == 'POST':
        city = request.form.get('city')
        state = request.form.get('state')
        country = request.form.get('country')
        
        if city and country:
            api_key = os.getenv('WEATHER_KEY')  # I saved my key in .env file
            print(api_key)  # This will print the key in the console or None
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city},{state},{country}&appid={api_key}&units=metric"
            response = requests.get(url)
            print(response.text)
            if response.status_code == 200:
                weather_data = response.json()
            else:
                error_message = "Unable to fetch weather data. Please check your inputs."
        else:
            error_message = "City and Country are required."
    
    return render_template('index.html', weather_data=weather_data, error_message=error_message)