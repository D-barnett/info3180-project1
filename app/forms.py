from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextField, PasswordField, RadioField, TextAreaField, IntegerField, SubmitField, FileField
from flask_wtf.file import FileField, FileRequired
from wtforms.validators import InputRequired, Email
from models import db, UserProfile

class ProfileForm(FlaskForm):
    username = TextField('Username', validators=[InputRequired()])
    first_name = TextField('Firstname', validators=[InputRequired()])
    last_name = TextField('Lastname', validators=[InputRequired()])
    age = TextField('Age', validators=[InputRequired()])
    biography = TextAreaField('Biography', validators=[InputRequired()])
    email = TextField('Email', validators=[InputRequired(), Email()])
    image = FileField('Image', validators=[FileRequired()])
    gender = SelectField('Gender', choices = [('M','Male'),('F','Female')], validators=[InputRequired()])
    
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    email = TextField('Email', validators=[InputRequired(), Email()])
    
    #def __init__(self, *args, **kwargs):
    #   FlaskForm.__init__(self, *args, **kwargs)
    
    def validate(self):
      if not FlaskForm.validate(self):
        return False
     
      user = UserProfile.query.filter_by(email = self.email.data.lower()).first()
      if user:
        self.email.errors.append("That email is already taken")
        return False
      else:
        return True
    
    
    
    