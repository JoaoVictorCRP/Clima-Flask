import requests
import string
from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)
API_KEY = os.getenv('API_KEY')

def get_weather_data(city):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=pt_br'
    response = requests.get(url).json()
    # print(response)
    return response

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