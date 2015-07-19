from flask import Flask, render_template  # , send_from_directory
# import os
import json

app = Flask(__name__)


# @app.route('/pass_data.js')
# def js():
#     stuff = "greasy"
#     return send_from_directory(os.path.join(app.root_path, 'static'),
#                                'pass_data.js', stuff=stuff)


@app.route("/")
def get_data():
    # a sample data set to for options to an html select.
    my_data = ["Uncle Lou's Sweet Spicy Love", "Diek's Wings of the Chicken", "Asian Flame Throwers", "Twisted BBQ", "Dusted and Crispy"]
    return render_template('data.html', my_data=json.dumps(my_data))


if __name__ == '__main__':
    app.run(debug=True)
