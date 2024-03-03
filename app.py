from flask import Flask, render_template, request, redirect, url_for, flash
import requisitions as r

app = Flask(__name__)

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