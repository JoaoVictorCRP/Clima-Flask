from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy as sqla
from sqlalchemy import Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Mapped, mapped_column
import requisitions as r

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clima.db'

# Classe relacional
# Base = declarative_base()

db = sqla(model_class=Base)
db.init_app(app)

# Modelo da cidade no banco de dados
class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

# Rota Principal
@app.route('/', methods=['GET','POST'])
def index():
    data = None # Declarando
    if request.method == 'POST':
        city = request.form['cityName']
        state = request.form['stateName']
        country = request.form['countryName']
        lat, lon = r.get_geolocation(city,state,country)
        data = r.get_weather_data(lat,lon)
    return render_template('index.html',data=data)

# Rota de Post
def index_post():
    msg_erro = ''
    city = request.form.get('cityName') # GET (** name do input **)
    city = city.lower()

# Criando o modelo
with app.app_context():
    db.create_all()
    test = db.session.execute(db.select(City).order_by(City.name)).scalars()



if __name__ == '__main__':
    app.run(debug=True)