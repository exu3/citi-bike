from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('map_legend.html', map="/static/bike_type.html", desc="wheeeee")


@app.route("/lcft")
def lcft():
    return render_template("map_legend.html",
                           map="/static/lcft.html",
                           desc="This map visualizes the various trips using line colors based on time of day. " +
                           "Each 3-hour block of the day has a designated color. For example, trips started between " +
                           "8pm and 11pm are navy blue, and trips around sunrise and in the morning are yellow and orange respectively.")


@app.route("/bike_type")
def bike_type():
    return render_template("map_legend.html",
                           map="/static/bike_type.html",
                           desc="This map shows the types of bikes used on various trips. " +
                           "The blue lines represent classic bikes, and the yellow lines repesent electric bikes. " +
                           "The lines connect start points and endpoints together linearly.")


@app.route("/histogram")
def histogram():
    return render_template("map_legend.html", map="/static/histogram.html", desc="histogram")


@app.route("/scatter")
def scatter():
    return render_template("map_legend.html", map="/static/scatter.html", desc="scatteeeerrrrrrrr")


if __name__ == '__main__':
    app.run(debug=True)
