from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo

class ApiCharForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description =  StringField('Description', validators=[DataRequired()])
    comics_appeared_in =  StringField('Comics Appeared In', validators=[DataRequired()])
    super_power =  StringField('Super Power', validators=[DataRequired()])
    submit = SubmitField()