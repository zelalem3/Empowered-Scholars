from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import bleach
import datetime
from datetime import timedelta
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

current_year = datetime.datetime.now().year
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///empweredscholarss.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "the secret key"
db = SQLAlchemy(app)

PERMANENT_SESSION_LIFETIME = timedelta(seconds=28800)
# Email configuration
smtp_server = 'smtp.gmail.com'
smtp_port = 587
username = 'z88812586@gmail.com'
app_password = 'jkij szcm bfif shuk'

    # Create the email content
msg = MIMEMultipart()
msg['From'] = username
msg['To'] = 'Empoweredscholarss@gmail.com'
msg['Subject'] = 'Form submitted'


class Data( db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(25), nullable=False)
    last_name = db.Column(db.String(25), nullable=False)
    phone_number = db.Column(db.String(12), nullable=False)
    email = db.Column(db.String(30), nullable=False, unique=True)
    message = db.Column(db.String(30), nullable=False, unique=True)


    def __repr__(self):
        return f'<User {self.first_name} {self.last_name}>'

class Report( db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(25), nullable=False)
    last_name = db.Column(db.String(25), nullable=False)
    phone_number = db.Column(db.String(12), nullable=False)
    email = db.Column(db.String(30), nullable=False, unique=True)
    education = db.Column(db.String(30), nullable=False, unique=True)
    birthday = db.Column(db.String(30))

    def __repr__(self):
        return f'<User {self.first_name} {self.last_name}>'



@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")




@app.route("/form", methods=["GET"])
def form():
    return render_template("form.html")





@app.route("/form", methods=["POST"])
def form_submit():
    fname = bleach.clean(request.form['fname'])
    lname = bleach.clean(request.form['lname'])
    phone_number = bleach.clean(request.form['phone_number'])
    email = bleach.clean(request.form['email'])
    education= bleach.clean(request.form["education"])
    birthday = bleach.clean(request.form["birthday"])

    # new_form = Report(
    #     first_name=fname,
    #     last_name=lname,
    #     phone_number=phone_number,
    #     email=email,
    #     birthday=birthday,
    #     education=education
    # )
    # db.session.add(new_form)
    # db.session.commit()

    # Body of the email
    body = f'A New form has been submmited By {fname} {lname} \n' \
           f'Email: {email} \n' \
           f'Phone_number: {phone_number} \n' \
           f'Education: {education} \n' \
           f'Birthday: {birthday}'

    msg.attach(MIMEText(body, 'plain'))

    # Send the email
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Secure the connection
        server.login(username, app_password)
        server.send_message(msg)
        flash('Form submitted successfully!', 'success')
        print('Email sent successfully!')
    except Exception as e:
        print(f'Error: {e}')
    finally:
        server.quit()
    return redirect(url_for('home'))




@app.route("/contact",methods=["GET"])
def contact():
    return  render_template("contact.html")






@app.route("/about", methods=["GET"])
def about():
    return render_template("about.html")











@app.route("/faq", methods=["GET"])
def faq():
    return render_template("FAQ2.html")










@app.route("/submit",methods=["POST"])
def get_form():
    fname = bleach.clean(request.form['fname'])
    lname = bleach.clean(request.form['lname'])
    phone_number = bleach.clean(request.form['phone_number'])
    email = bleach.clean(request.form['email'])
    message = bleach.clean(request.form["message"])

    # new_form = Data(
    #         fname=fname,
    #         lname=lname,
    #         phone_number=phone_number,
    #         email=email,
    #         message=message
    # )
    # db.session.add(new_form)
    # db.session.commit()

    # Body of the email
    body = f'A New for has been submmited By {fname} {lname} \n' \
           f'Email: {email} \n' \
           f'Phone_number: {phone_number} \n' \
           f'Message: {message} \n'

    msg.attach(MIMEText(body, 'plain'))

    # Send the email
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Secure the connection
        server.login(username, app_password)
        server.send_message(msg)
        flash("successfully submitted the form")
        print('Email sent successfully!')
    except Exception as e:
        print(f'Error: {e}')
    finally:
        server.quit()

    flash("form submitted successfully")
    # db.session.add(new_form)
    # db.session.commit()


    return redirect(url_for(home))












if __name__ == "__main__":
    app.run(debug=True, port=5000)


