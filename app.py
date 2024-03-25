from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy as sqla
from sqlalchemy import Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Mapped, mapped_column
import requisitions as r

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clima.sqlite3'

db = sqla(app)

# Modelo da cidade no banco de dados
class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(40))
    country = db.Column(db.String(50))

    def __init__(self, name, state=None,country=None) -> None:
        self.name = name
        if state:
            self.state = state
        if country:
            self.country = country

# Rota Principal
@app.route('/', methods=['GET','POST'])
def index():
    cities = City.query.all()
    weather_data = []
    data = None # Declarando
    
    for city in cities:
        # Está ocorrendo algum erro de iteração aqui, algum 
        if city.name:
            print(f'{city.name} deu certo.') # debug
            lat, lon = r.get_geolocation(city.name,city.state,city.country)
            data = r.get_weather_data(lat,lon)
            weather_data.append(data)

    if request.method == 'POST':
        city = request.form['cityName']
        state = request.form['stateName']
        country = request.form['countryName']
        # Saving Data
        queried_city = City(city, state, country)
        db.session.add(queried_city)
        db.session.commit()
        # Querying Data
        lat, lon = r.get_geolocation(city,state,country)
        data = r.get_weather_data(lat,lon)
        weather_data.insert(1,data)
    return render_template('index.html',weather_data=weather_data)

# Rota de Post
def index_post():
    msg_erro = ''
    city = request.form.get('cityName') # GET (** name do input **)
    city = city.lower()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)