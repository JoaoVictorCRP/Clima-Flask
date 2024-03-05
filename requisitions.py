import requests
import os
from dotenv import load_dotenv
from dataclasses import dataclass

load_dotenv()
API_KEY = os.getenv('API_KEY')

@dataclass
class WeatherData:
    '''Objeto de resposta da API'''
    name: str
    main: str
    description: str
    icon: str
    temperature: float

def get_geolocation(city: str, state: str, country: str):
    try: 
        url = f'http://api.openweathermap.org/geo/1.0/direct?q={city},{state},{country}&limit=1&appid={API_KEY}'
        response = requests.get(url).json()[0]
        lat, lon = response.get('lat'), response.get('lon')
        
        return lat, lon
    except Exception as e:
        print(f'Requisição da geolocalização falhou!\n{e}')

# Função de Requisição do Clima
def get_weather_data(lat, lon):
    try:
        url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric&lang=pt_br'
        response = requests.get(url).json()
        data = WeatherData(
            name=response.get('name'),
            main=response.get('weather')[0].get('main'), # "Main" é a definição do clima, essa parte pode ser traduzida de acordo com os parametros da requisição
            description=response.get('weather')[0].get('description'),
            icon=response.get('weather')[0].get('icon'),
            temperature=int(response.get('main').get('temp'))
        )
        return data
    except Exception as e:
        print(f'Requisição do clima falhou!\n{e}')