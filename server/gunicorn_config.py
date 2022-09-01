import gunicorn


max_requests = 1000
max_requests_jitter = 50
gunicorn.SERVER = "wfapi-prod"
print(f"Starting server => {gunicorn.SERVER}")
workers = 4
accesslog = "api.log"
errorlog = "app.log"
loglevel = "debug"
capture_output = True
bind = '0.0.0.0:5000'