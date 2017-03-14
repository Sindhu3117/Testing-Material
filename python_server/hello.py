from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/201")
def ret_201():
    return "Hello World!", 201

if __name__ == "__main__":
    app.run()
