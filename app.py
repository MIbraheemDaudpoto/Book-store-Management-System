from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database Configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///BooksDataBase.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(100), unique=True, nullable=False)

    author = db.Column(db.String(100), nullable=False)

    category = db.Column(db.String(100), nullable=False)

    price = db.Column(db.Integer, nullable=False)

    quantity = db.Column(db.Integer, nullable=False)


# Create Database
with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)