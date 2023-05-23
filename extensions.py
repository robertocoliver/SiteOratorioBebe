from flask_sqlalchemy import SQLAlchemy
from flaskext.mysql import MySQL
from flask_mysqldb import MySQL

db = SQLAlchemy()
mysql = MySQL()


def init_app(app):
    db.init_app(app)
    mysql.init_app(app)

    
