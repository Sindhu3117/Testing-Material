import json
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
    return 'Hello Sindhu! data 404 Page not found', 404

@app.route("/404")
def ret_404():
    # Sending status code 404
    abort(404)

@app.errorhandler(500)
def internal_server_error(e):
    return 'Hello Sindhu! data 500 internal server error', 500
    # return 'Hello Sindhu!', 200

@app.route("/500")
def ret_500():
    # Sending status code 500
    raise 'Error'

@app.route("/simple_dict_json")
def ret_simple_dict_json():
    # Sending json
    sample_dict = {'name': 'Sindhu'}
    print json.dumps(sample_dict, indent=2)
    return str(sample_dict)

@app.route("/dogs_list_json")
def ret_dogs_list_json():
    # Sending json
    sample_dict = ['panda', 'mish', 'tina', 'juli']
    print json.dumps(sample_dict, indent=2)
    return str(sample_dict)

@app.route("/list_of_objs_json")
def ret_list_of_objs_json():
    # Sending json
    sample_dict = [{'name': 'Sindhu'}, {'name': 'Veer'}, {'name': 'pandi'}]
    print json.dumps(sample_dict, indent=2)
    return str(sample_dict)

@app.route("/objs_having_lists_json")
def ret_objs_having_lists_json():
    # Sending json
    sample_dict = {'names': ['Sindhu', 'Ujwala', 'Veer'],
                   'dogs': ['panda', 'mish', 'tina', 'juli']}
    print json.dumps(sample_dict, indent=2)
    return str(sample_dict)

@app.route("/objs_having_objs_json")
def ret_objs_having_objs_json():
    # Sending json
    sample_dict = {'humans': {'names':['Sindhu', 'Ujwala', 'Veer'],
                              'ages': [70, 70, 32]},
                   'dogs': ['panda', 'mish', 'tina', 'juli']}
    print json.dumps(sample_dict, indent=2)
    return str(sample_dict)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
