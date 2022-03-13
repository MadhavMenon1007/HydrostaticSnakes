from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from forms import PatientEntry

app = Flask(__name__)
app.config["SECRET_KEY"] = "4a0f2618ecf89b6e57bc979ec5b246bbbb45a9d332f4a0510b1607bbc0b064c4" # Makes our app more secure
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:Pookie10_@localhost/patientinformation" 

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
    attenders_code = db.Column(db.String, nullable=False)
    ambulance_licenceplate = db.Column(db.String, nullable = False)

    def __init__(self, patient_id, name, age, gender, blood_type, injury_type, injury_location, injury_cause, heart_rate, o2_level, attenders_code, ambulance_licenceplate):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.blood_type = blood_type
        self.injury_type = injury_type
        self.injury_location = injury_location
        self.injury_cause = injury_cause
        self.heart_rate = heart_rate
        self.o2_level = o2_level
        self.attenders_code = attenders_code
        self.ambulance_licenceplate = ambulance_licenceplate

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
    # if flask_form.validate_on_submit():
    #     flash(f'The details of {flask_form.name.data} have been submitted successfully', "success")
    #     return render_template("success.html")
    return render_template("patient_entry.html", form = flask_form, title = "Patient Entry")

@app.route("/submit", methods=["GET", "POST"])
def submit():
    id= 1
    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]
        gender = request.form["gender"]
        blood_type = request.form["blood_type"]
        injury_type = request.form["injury_type"]
        injury_location = request.form["injury_location"]
        injury_cause = request.form["injury_cause"]
        heart_rate = request.form["heart_rate"]
        o2_level = request.form["o2_level"]
        attenders_code = request.form["attenders_code"]
        ambulance_licenceplate = request.form["ambulance_licenceplate"]
        patient = Patient(patient_id = id, name = name, age = age, gender = gender, blood_type = blood_type, injury_type = injury_type, injury_location = injury_location, injury_cause = injury_cause, heart_rate = heart_rate, o2_level = o2_level, attenders_code = attenders_code, ambulance_licenceplate = ambulance_licenceplate)
        db.session.add(patient)
        db.session.commit()
        id+=1
    return render_template("success.html")


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

 