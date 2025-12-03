# weather.py

import requests
from django.conf import settings  # Importación de la configuración
import json # Necesario si la data no se carga bien

def get_weather_info(city="Medellin"):
    #CAMBIO CLAVE: Usamos django.conf.settings
    api_key = settings.WEATHER_API_KEY
    
    #Verificación de clave
    if not api_key:
        print("ERROR: WEATHER_API_KEY no está definida en settings.py")
        return 24, "Clima no disponible (Usando valor de prueba)" # Valor seguro de fallback
        
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status() # Lanza un error para códigos 4xx/5xx
        data = response.json()
        
        temp_celsius = data['current']['temp_c']
        condition = data['current']['condition']['text']
        return temp_celsius, condition
        
    except Exception as e:
        print(f"Error obteniendo clima: ({e})")
        # Devolvemos un valor seguro (fallback) si la API falla
        return 24, "Error al consultar API (Usando valor de prueba)"