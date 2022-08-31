from flask import Flask,request, render_template, send_from_directory # Add render_template
import fix_index
from server.providers.log_provider import logger

fix_index.fixIndexHTMLdoc()

app = Flask(__name__)


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

@app.route("/api/")
def my_api():
    return "hi"

@app.errorhandler(500)
def server_error(e):
  return 'An internal error occurred [main.py] %s' % e, 500       

if __name__ == '__main__':
  logger.info("Application started in DEV mode")
  app.run()

