from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy as sqla
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
import requisitions as r


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clima.db'
db = sqla(app)

# Modelo da cidade no banco de dados
class City(db.Model):
    __tablename__ = 'cities',
    id: Mapped[int] = mapped_column(primary_key=True)
    city: Mapped[str] = mapped_column(nullable=False)

# Criando o modelo
with app.app_context():
    db.create_all()

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



if __name__ == '__main__':
    app.run(debug=True)