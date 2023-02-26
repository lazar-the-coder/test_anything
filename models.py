from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pets.db'
db.init_app(app)

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column("Created", db.DateTime, default=datetime.datetime.now)
    name = db.Column("Name", db.String())
    age = db.Column("Age", db.String())
    breed = db.Column("Breed", db.String())
    color = db.Column("Color", db.String())
    size = db.Column("Size", db.String())
    weight = db.Column("Weight", db.String())
    url = db.Column("URL", db.String())
    url_tag = db.Column("Alt Tag", db.String())
    pet_type = db.Column("Pet Type", db.String())
    gender = db.Column("Gender", db.String())
    spay = db.Column("Spay", db.String())
    house_trained = db.Column("House Trained", db.String())
    description = db.Column("Description", db.Text)

    def __ref__(self):
        return f'''Pet (Name: {self.name})'''