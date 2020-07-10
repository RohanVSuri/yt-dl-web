from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, RadioField
from wtforms.validators import DataRequired

class Form(FlaskForm):
    link = StringField("Link!!", validators=[DataRequired()])
    submit = SubmitField("Submit", validators=[DataRequired()])

    metadata = BooleanField("MetaData?", validators=[DataRequired()])
    title = StringField("Title")
    artist = StringField("Artist")
    album = StringField("Album")
