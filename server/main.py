from flask import Flask,jsonify, request, render_template, send_from_directory # Add render_template
import fix_index
from server.controllers import EntitiesResource, EntityResource
from server.providers.log_provider import logger
from flask_restful import Resource, Api

from werkzeug.http import HTTP_STATUS_CODES
from werkzeug.exceptions import HTTPException


fix_index.fixIndexHTMLdoc()

errors = {
    'Conflict': {
        'message': "A user with that username already exists.",
        'status': 409,
    },
}

app = Flask(__name__)
api = Api(app, errors=errors)



@app.route('/<path:path>', methods=['GET'])
def static_proxy(path):
  print("This is the path => " + path)
  return render_template("index.html")


@app.route('/')
def hello_world():
  if request.args:
      key = list(request.args)[0]
      return send_from_directory("./static", key)
  else:
    return send_from_directory('./static', 'index.html')


@app.errorhandler(500)
def server_error(e):
  return f'An internal error occurred [main.py] {str(e)}', 500   

api.add_resource(EntitiesResource, "/entity/<string:entity>")
api.add_resource(EntityResource, "/entity/<string:entity>/<string:id>")



if __name__ == '__main__':
  logger.info("Application started in DEV mode")
  app.run()

