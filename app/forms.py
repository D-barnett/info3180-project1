from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextField, PasswordField, RadioField, TextAreaField, IntegerField, SubmitField, FileField
from flask_wtf.file import FileField, FileRequired
from wtforms.validators import InputRequired


class ProfileForm(FlaskForm):
    username = TextField('Username', validators=[InputRequired()])
    first_name = TextField('Firstname', validators=[InputRequired()])
    last_name = TextField('Lastname', validators=[InputRequired()])
    age = TextField('Age', validators=[InputRequired()])
    biography = TextAreaField('Biography', validators=[InputRequired()])
    image = FileField('Image', validators=[FileRequired()])
    gender = SelectField('Gender', choices = [('M','Male'),('F','Female')], validators=[InputRequired()])
    submit = SubmitField('Send')
    
    