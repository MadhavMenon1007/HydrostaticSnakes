from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm, PatientEntry

app = Flask(__name__)
app.config["SECRET_KEY"] = "4a0f2618ecf89b6e57bc979ec5b246bbbb45a9d332f4a0510b1607bbc0b064c4" # Makes our app more secure

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title = "Medbridge")

@app.route("/about")
def about():
    return render_template("about.html", title = "About Us")

@app.route("/patiententry")
def patient_entry():
    form = PatientEntry()
    return render_template("patient_entry.html", form = form, title = "Patient Entry")


@app.route("/registration")
def registration():
    form = RegistrationForm() # Creates a registration form at the registration page
    return render_template("registration.html", form = form, title = "Registration")

@app.route("/login")
def login():
    form = LoginForm() 
    return render_template("login.html", form = form, title = "Login")

if __name__ == "__main__":
    app.run(debug = True)

 