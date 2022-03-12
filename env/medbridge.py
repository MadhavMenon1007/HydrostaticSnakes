from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from forms import PatientEntry

app = Flask(__name__)
app.config["SECRET_KEY"] = "4a0f2618ecf89b6e57bc979ec5b246bbbb45a9d332f4a0510b1607bbc0b064c4" # Makes our app more secure
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///patients.db"
db = SQLAlchemy(app) # Creates database

class Patient(db.Model): 
    patient_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable = False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String, nullable=False)
    blood_type = db.Column(db.String(3), nullable=False)
    injury_type = db.Column(db.String, nullable=False)
    injury_location = db.Column(db.String, nullable=False)
    injury_cause = db.Column(db.String, nullable=False)
    heart_rate = db.Column(db.Integer, nullable=False)
    o2_level = db.Column(db.Integer, nullable=False)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title = "Medbridge")

@app.route("/about")
def about():
    return render_template("about.html", title = "About Us")

@app.route("/patiententry", methods=["GET", "POST"])
def patient_entry():
    flask_form = PatientEntry()
    if flask_form.validate_on_submit():
        flash(f"{flask_form.name.data}'s details have been submitted successfully", "success")
        return redirect(url_for("home"))
    return render_template("patient_entry.html", form = flask_form, title = "Patient Entry")

# @app.route("/registration")
# def registration():
#     flask_form = RegistrationForm() # Creates a registration form at the registration page
#     return render_template("registration.html", form = form, title = "Registration")

# @app.route("/login")
# def login():
#     flask_form = LoginForm() 
#     return render_template("login.html", form = form, title = "Login")

if __name__ == "__main__":
    app.run(debug = True)

 