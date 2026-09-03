from flask import Flask

app = Flask(__name__) # creates an instance of a Flask server from the built-in python variable __name__
@app.route("/") # when the http request is made to the Flask server, this what the browser needs to send when it is making the request
def home():
    return "Hello, from Flask!" 

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)