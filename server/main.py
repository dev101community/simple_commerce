from flask import Flask,jsonify, request, Response, render_template, send_from_directory # Add render_template
from server.controllers import EntitiesResource, EntityResource
from server.providers.log_provider import logger
from flask_restful import Resource, Api
from flask_cors import CORS

from werkzeug.http import HTTP_STATUS_CODES
from werkzeug.exceptions import HTTPException


app = Flask(__name__)
CORS(app)
api = Api(app)



@app.route('/')
def hello_world():
  return "pong"


@app.errorhandler(500)
def server_error(e):
  return f'An internal error occurred [main.py] {str(e)}', 500   

api.add_resource(EntitiesResource, "/<string:entity>")
api.add_resource(EntityResource, "/<string:entity>/<string:id>")


if __name__ == '__main__':
  logger.info("Application started in DEV mode")
  app.run()

