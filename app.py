from flask import Flask
from config import Config
from flask import Blueprint
from routes import bp as routes_bp
from model import db


app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

app.register_blueprint(routes_bp, name='routes_bp')
@app.after_request
def headers(response):
    #response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains' #adicionar HSTS primeiro
    #response.headers['Content-Security-Policy'] = "script-src 'none'"
    response.headers['Content-Security-Policy'] = "default-src 'self'"
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['Referrer-Policy'] = 'no-referrer'
    return response 


app.register_blueprint(routes_bp)


