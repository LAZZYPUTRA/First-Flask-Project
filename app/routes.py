from flask import render_template
from app import app
@app.route("/")
def home() :
    hello = "hello world"
    return render_template("index.html", hello=hello)

if __name__ == "__main__" :
    app.run(debug=True)
