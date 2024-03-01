import requests
from flask import Flask, render_template, request, redirect, url_for, flash
import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')
app = Flask(__name__)

@dataclass
class WeatherData:
    '''Objeto de resposta da API'''
    main: str
    description: str
    icon: str
    temperature: float

def get_weather_data(city):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=pt_br'
    response = requests.get(url).json()
    data = WeatherData(
        main=response.get('weather')[0].get('main'), # Definição do clima, em inglês
        description=response.get('weather')[0].get('description'),
        icon=response.get('weather')[0].get('icon'),
        temperature=response.get('main').get('temp')
    )
    return data

# Rota Principal
@app.route('/')
def get_index():
    return render_template('index.html')

# Rota de Post
def index_post():
    msg_erro = ''
    city = request.form.get('cidade') # GET (** name do input **)
    city = city.lower()
    # FAZER A REQUISIÇÃO DA CIDADE PEDIDA...


if __name__ == '__main__':
    print(get_weather_data('Sao Paulo').description)