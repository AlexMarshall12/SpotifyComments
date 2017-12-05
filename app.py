from flask import Flask,render_template
from flas_sqlalchemy import SQLAlchemy

app = Flask('myapplication')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////test.db'
db = SQLAlchemy(app)

class Song(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    spotify_id = db.Column(db.String(80),unique=True,nullable=False)

class Comment(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    content = db.Column(db.String(140))

@app.route('/')
def index():
    return render_template(index.html)

@app.route('/<songid>'>
def song_page(songid):
     
    sqlite.query(get tha

def db_init():        
    db.create_all()

