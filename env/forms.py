from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, FloatField
from wtforms.validators import Length, Email, DataRequired, EqualTo # Validators used to ensure that data conforms to certain formats

# class RegistrationForm(FlaskForm): # Creates the registration form
#     name = StringField("Hospital Name", validators = [Length(min=10, max=30), DataRequired()]) 
#     email = StringField("Hospital Email", validators = [Email(), DataRequired()])
#     password = PasswordField("Password", validators = [Length(min=10), DataRequired()])
#     password_verification = PasswordField("Password Verification", validators = [EqualTo("password"), DataRequired()])
#     submit_button = SubmitField("Register as a hospital")

# class LoginForm(FlaskForm): 
#     name = StringField("Hospital Name", validators = [Length(min=10, max=30), DataRequired()])
#     email = StringField("Hospital Email", validators = [Email(), DataRequired()])
#     password = PasswordField("Password", validators = [Length(min=10), DataRequired()])
#     submit_button = SubmitField("Login")


class PatientEntry(FlaskForm): 
    name = StringField("Patient Name", validators = [DataRequired()])  
    age = IntegerField("Patient Age", validators = [DataRequired()])
    gender = StringField("Patient Gender", validators = [DataRequired()])
    blood_type = StringField("Blood Type", validators = [DataRequired(), Length(max=3)])
    injury_type = StringField("Type of injury", validators = [DataRequired()])
    injury_location = StringField("Location of injury", validators = [DataRequired()])
    injury_cause = StringField("Cause of injury", validators = [DataRequired()])
    heart_rate = IntegerField("Heart rate", validators = [DataRequired()])
    o2_level = FloatField("Oxygen level", validators = [DataRequired()])
    attenders_code = StringField("First Attender's code", validators = [DataRequired(), Length(min = 2, max=20)])
    ambulance_licenceplate = StringField("Ambulance's Licence plate", validators = [DataRequired()])
    submit_button = SubmitField("Submit Patient")


