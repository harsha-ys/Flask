from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Home Page"

@app.route("/about")# endpoint api otherthan home
def about():
    return "About Page"

if __name__ == "__main__" :
    app.run(debug=True)