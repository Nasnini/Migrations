from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config['SQLALCHEMY_DATATBASE_URI'] = 'postgresql://pguser:password@127.0.0.1/development'
db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

class development(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(25))
    surname = db.Column(db.String(25))
    chat_name = db.Column(db.String(25))
    github_name = db.Column(db.String(25))
    id_number = db.Column(db.Integer(13))
    dev =db.relationship('Dev', backref='owner', lazy='dynamic')

if __name__ == '__main__':
    manager.run()

