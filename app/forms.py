from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    link = StringField("Link!!", validators=[DataRequired()])
    submit = SubmitField("Submit", validators=[DataRequired()])
    metaa = BooleanField("MetaData?", validators=[DataRequired()])
