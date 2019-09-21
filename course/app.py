from flask import Flask, render_template
#from flask_flatpages import FlatPages
from flask_frozen import Freezer


app = Flask(__name__)
app.config.from_pyfile('settings.py')
#pages = FlatPages(app)
freezer = Freezer(app)

@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
