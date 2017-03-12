from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, RadioField, TextAreaField, IntegerField, SubmitField, FileField
from flask_wtf.file import FileField, FileRequired
from wtforms.validators import InputRequired


class ProfileForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    first_name = StringField('Firstname', validators=[InputRequired()])
    last_name = StringField('Lastname', validators=[InputRequired()])
    age = IntegerField('Age', validators=[InputRequired()])
    biography = TextAreaField('Biography', validators=[InputRequired()])
    image = FileField('Image', validators=[FileRequired()])
    gender = RadioField('Gender', choices = [('M','Male'),('F','Female')], validators=[InputRequired()])
    submit = SubmitField('Send')
    
    