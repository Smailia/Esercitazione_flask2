from flask import Flask, request, render_template
app = Flask(__name__)
lista =  1,2,3,3,4,4,4,5,5,6,6,6,6

@app.route("/")
def home():
    return render_template('index.html', lista = lista)
@app.route("/profilo")
def profilo():
   return "questa è la pagina profilo"


if __name__ == '__main__':
    app.run(debug=True)