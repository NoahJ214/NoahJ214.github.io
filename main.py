# import "packages" from flask

from waitress import serve
# create a Flask instance
app = Flask(__name__)
app.register_blueprint(app_api)
app.register_blueprint(nfl_nfl)

# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")


# connects /kangaroos path to render kangaroos.html
@app.route('/timmy/')
def Timmy():
    return render_template("timothy.html")


@app.route('/ritvik/', methods=['GET', 'POST'])
def Ritvik():
    return render_template("ritvik.html")



@app.route('/nathan/')
def Nathan():
    return render_template("nathan.html")

@app.route('/william/')
def William():
    return render_template("william.html")

@app.route('/noah/')
def Noah():
    return render_template("noah.html")

# @app.route('/basketball/', methods=['GET', 'POST'])
# def basketball():
 #   url = "http://localhost:5000/api/basketball_api"
 #   response = requests.request("GET", url)
 #   return render_template("ritvik.html")

# runs the application on the development server
if __name__ == "__main__":
    #app.run(debug=True)
    serve(app, host='0.0.0.0', port=80)
