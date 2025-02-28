import requests
import json

# openmweather api key
API_KEY = 'e6ecf5dcba21b4f6a60bddc6e647f9ee'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

def get_weather(city):
    
    try:
         
        # params=params tells Python to attach the parameters to the request
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status() # This checks if the request was successful
        
        data = response.json()
        
        weather = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'description': data['weather'][0]['description'],
            'wind_speed': data['wind']['speed']
        }
        
        return weather
    
    except requests.exceptions.RequestException as e:
        print('\n⚠️ Network error! Please check yor internet conection')
        print(f'Error details : {e}')
        return None
    
    except KeyError:
        print('\n❌ City not found! Please enter a valid city name.')
        return None
    

        
    
        
        
        