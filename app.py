from flask import Flask, render_template, request, redirect, url_for, flash
from weather import get_weather_data

app = Flask(__name__)

# Rota Principal
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        city = request.form['cidade']
        print(get_weather_data(city))
    return render_template('index.html')

# Rota de Post
def index_post():
    msg_erro = ''
    city = request.form.get('cidade') # GET (** name do input **)
    city = city.lower()


if __name__ == '__main__':
    app.run(debug=True)