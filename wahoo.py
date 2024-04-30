from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('map_legend.html', map="./bike_type.html")


@app.route("/lfct")
def lfct():
    return render_template("map_legend.html", map="/static/lfct.html")


@app.route("/bike_type")
def bike_type():
    return render_template("map_legend.html", map="/static/bike_type.html")

# from flask import Flask, render_template

# app = Flask(__name__)

# # Route to render the default map view
# @app.route('/')
# def index():
#     return render_template('map_view1.html')

# # Route to render the second map view
# @app.route('/map2')
# def map2():
#     return render_template('map_view2.html')

# # Route to render the third map view
# @app.route('/map3')
# def map3():
#     return render_template('map_view3.html')

# if __name__ == '__main__':
#     app.run(debug=True)
