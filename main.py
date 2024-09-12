from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import bleach
import datetime
from datetime import timedelta
current_year = datetime.datetime.now().year
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///empweredscholarss.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "the secret key"
db = SQLAlchemy(app)

PERMANENT_SESSION_LIFETIME = timedelta(seconds=28800)


class Data( db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(25), nullable=False)
    last_name = db.Column(db.String(25), nullable=False)
    phone_number = db.Column(db.String(12), nullable=False)
    email = db.Column(db.String(30), nullable=False, unique=True)
    message = db.Column(db.String(30), nullable=False, unique=True)


    def __repr__(self):
        return f'<User {self.first_name} {self.last_name}>'



@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")



@app.route("/contact",methods=["GET"])
def contact():
    return  render_template("contact.html")

@app.route("/about", methods=["GET"])
def about():
    return render_template("about.html")


@app.route("/form", methods=["GET"])
def about():
    return render_template("form.html")



@app.route("/submit",methods=["POST"])
def get_form():
    fname = bleach.clean(request.form['fname'])
    lname = bleach.clean(request.form['lname'])
    phone_number = bleach.clean(request.form['phone_number'])
    email = bleach.clean(request.form['email'])
    message = bleach.clean(request.form["message"])

    new_form = Data(
            fname=fname,
            lname=lname,
            phone_number=phone_number,
            email=email,
            message=message
    )
    flash("form submitted successfully")
    db.session.add(new_form)
    db.session.commit()


    return redirect(url_for(home))


if __name__ == "__main__":
    app.run(debug=True, port=5000)


