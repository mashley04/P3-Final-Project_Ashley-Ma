## Ashley Ma
## HCDE 310
## P3:FINAL PROJECT


import functions
from flask import Flask, render_template, request

# Create an instance of Flask
app = Flask(__name__)

# Create a view function for /
@app.route("/")
def index():
    return render_template("index.html")


# Create a view function for /results
@app.route("/results", methods=["GET", "POST"])
def results():
    if request.method == "POST":
        pokemon = request.form["pokemon"]
        film = functions.film_info(pokemon)
        type = functions.pokemon_info(pokemon)
        pic = functions.pokemon_pic(pokemon)
        upper_name = functions.upper(pokemon)

        return render_template("results.html", film=film, pokemon = pokemon, type = type,
                               pic = pic, upper_name = upper_name)

    elif request.method == "GET":
        return "Wrong HTTP method", 400
