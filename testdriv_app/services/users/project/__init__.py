# services/users/project/__init__.py
import os
from flask import Flask, jsonify
import sys
# instantiate the app
app = Flask(__name__)

# set config
#app.config.from_object('project.config.DevelopmentConfig')
#update project/__init__.py, to pull in the environment variables
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)

#test & print log 
#print(app.config, file=sys.stderr)

@app.route('/users/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
        })
