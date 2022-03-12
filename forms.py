from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, Email, DataRequired, EqualTo # Validators used to ensure that data conforms to certain formats

class RegistrationForm(FlaskForm): # Creates the registration form
    name = StringField("Hospital Name", validators = [Length(min=10, max=30), DataRequired()]) 
    email = StringField("Hospital Email", validators = [Email(), DataRequired()])
    password = PasswordField("Password", validators = [Length(min=10), DataRequired()])
    password_verification = PasswordField("Password Verification", validators = [EqualTo("password"), DataRequired()])
    submit_button = SubmitField("Register as a hospital")

class LoginForm(FlaskForm): 
    name = StringField("Hospital Name", validators = [Length(min=10, max=30), DataRequired()])
    email = StringField("Hospital Email", validators = [Email(), DataRequired()])
    password = PasswordField("Password", validators = [Length(min=10), DataRequired()])
    submit_button = SubmitField("Login")


    
    