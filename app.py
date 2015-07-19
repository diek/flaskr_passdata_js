from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route("/")
def get_data():
    # a sample data set to for options to an html select.
    my_data = ["Uncle Lou's Sweet Spicy Love", "Diek's Wings of the Chicken", "Asian Flame Throwers", "Twisted BBQ", "Dusted and Crispy"]
    return render_template('data.html', my_data=json.dumps(my_data))


if __name__ == '__main__':
    app.run(debug=True)
