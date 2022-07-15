# здесь код для работы с flask-sqlalchemy, чтобы избежать проблем с circular dependencies

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
