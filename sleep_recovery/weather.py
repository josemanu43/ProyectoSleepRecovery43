import requests
from django.conf import settings

def get_weather_info(city="Medellin"):
    api_key = settings.WEATHER_API_KEY
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"
    
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        temp_celsius = data['current']['temp_c']
        condition = data['current']['condition']['text']
        return temp_celsius, condition

    except Exception as e:
        print(f"Error obteniendo clima: {e}")
        return None, "Desconocido"
