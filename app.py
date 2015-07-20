from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route("/")
def get_data():
    # a sample data set, for options for an html select.
    wing_options = ["Uncle Lou's Sweet Spicy Love", "Diek's Wings of the Chicken", "Asian Flame Throwers", "Twisted BBQ", "Dusted and Crispy"]
    return render_template('data.html', wing_options=json.dumps(wing_options))


if __name__ == '__main__':
    app.run(debug=True)
