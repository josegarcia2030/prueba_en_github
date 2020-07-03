from flask import Flask, render_template

app = Flask(__name__) #Archivo principal de la aplicacion, almacena en la variable app

@app.route('/') #Ruta para la pagina principal
def home():
    return render_template('home.html')

@app.route('/services') #Ruta para la pagina de servicios
def services():
    return render_template('services.html')

@app.route('/about') #Ruta para la pagina de about
def about():
    return render_template('about.html')



if __name__ == '__main__':
    app.run(debug=True)