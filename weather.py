import requests
import os
from dotenv import load_dotenv
from dataclasses import dataclass

load_dotenv()
API_KEY = os.getenv('API_KEY')

@dataclass
class WeatherData:
    '''Objeto de resposta da API'''
    main: str
    description: str
    icon: str
    temperature: float

# Função de Requisição
def get_weather_data(city: str):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=pt_br'
    response = requests.get(url).json()
    data = WeatherData(
        main=response.get('weather')[0].get('main'), # Definição do clima, em inglês
        description=response.get('weather')[0].get('description'),
        icon=response.get('weather')[0].get('icon'),
        temperature=response.get('main').get('temp')
    )
    return data