import flask
import sqlalchemy.sql
from flask import Flask, redirect, url_for, render_template, request, flash, send_from_directory, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey, Date


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:zael123456@localhost/app_nego'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'secret string'

db = SQLAlchemy(app)


app.config['DEBUG'] = True

class data_nego(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fournisseur = db.Column(db.String(150), nullable=False)
    categorie= db.Column(db.String(150), nullable=False)
    partie = db.Column(db.String(150), nullable=False)
    sous_partie = db.Column(db.String(150), nullable=False)
    commentaire = db.Column(db.String(600),  nullable=False)
    def __init__(self, fournisseur, categorie, partie,sous_partie, commentaire):
        self.fournisseur = fournisseur
        self.categorie = categorie
        self.partie = partie
        self.sous_partie = sous_partie
        self.commentaire = commentaire

@app.route('/')
def home():
   return render_template('home.html')


@app.route("/add", methods=['POST'])
def add_data():
    fournisseur = request.form["fournisseur"]
    categorie = request.form["categorie"]
    partie = request.form["partie"]
    sous_partie = request.form["sous_partie"]
    commentaire = request.form["commentaire"]
    entry = data_nego(fournisseur, categorie, partie,sous_partie, commentaire)
    db.session.add(entry)
    db.session.commit()
    return render_template("home.html")

@app.route('/list_data')
def list_data():
    socks = data_nego.query.order_by(-data_nego.id).limit(8).all()
    return render_template('list_data.html', socks=socks)

if __name__ == "__main__":
    db.create_all()
    app.run(host="0.0.0.0")

