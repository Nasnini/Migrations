import psycopg2
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

connection = psycopg2.connect(database="development", user="user", password="pass", host="localhost", port=5432)
cursor = connection.cursor()

# SQL Query - Insert into recruit
query = """ INSERT INTO recruit(first_name, surname, chat_name, github_name, id_number)
        VALUES
        ('Nasni', 'Smith', '@Nasni', 'github.com/Nasni', '9803249905811'),
        ('Tetelo', 'Mohapi', 'TTQueen', 'github.com/TTForever', '9209108040667'),
        ('Schubaica', 'Jenkies', 'Baiccah', 'github.com/baica', '0211309023497'),
        ('Peter', 'Brown', 'Pieter', 'github.com/PeeDawg', '85091528500369'),
        ('Tshepo', 'Mokoena', 'Batisah', 'github.com/BeastCode', '8704203549894')
        """

app = Flask(__name__)
app.config['SQLALCHEMY_DATATBASE_URI'] = 'postgresql://user:pass@127.0.0.1/development'
db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25))
    recruit = db.relationship('Recruit', backref='owner', lazy='dynamic')

class Recruit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(25))
    surname = db.Column(db.String(25))
    chat_name = db.Column(db.String(25))
    github_name = db.Column(db.String(25))
    id_number = db.Column(db.NUMERIC(13))
    #dev =db.relationship('Dev', backref='owner', lazy='dynamic')

# Executes instructed query method
cursor.execute(query)

# Commits all the scripts in the class to the connected database
connection.commit()
if __name__ == '__main__':
    manager.run()