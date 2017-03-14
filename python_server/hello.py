from flask import Flask, abort
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/201")
def ret_201():
    # Sending status code 201
    return "201 Data", 201

@app.errorhandler(404)
def page_not_found(e):
    return 'data 404 Page not found', 404

@app.route("/404")
def ret_404():
    # Sending status code 404
    abort(404)

@app.route("/500")
def ret_500():
    # Sending status code 500
    raise 'Error'

if __name__ == "__main__":
    app.run()
