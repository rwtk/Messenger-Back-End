import os

from flask import Flask
from flask import request
from flask_cors import CORS
from flask import jsonify


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/', methods=['GET'])
    def hello():
        response = jsonify({'message': 'Hello World!'})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    
    @app.route('/get-message', methods=['POST'])
    def get_message():
        if request.method == 'POST':
            number = request.form['messageID']
            if number == '1':
                response = jsonify({'message': 'This is message 1'})
                response.headers.add('Access-Control-Allow-Origin', '*')
                return response

    return app