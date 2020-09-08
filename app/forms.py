from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, RadioField
from wtforms.validators import DataRequired

class DownloadForm(FlaskForm):
    link = StringField("Link!!", validators=[DataRequired()])
    submit = SubmitField("Submit", validators=[DataRequired()])
    
    metadata = BooleanField("MetaData?", validators=[DataRequired()])
    convert = BooleanField("Convert to mp3?", validators=[DataRequired()])
    title = StringField("Title")
    artist = StringField("Artist")
    album = StringField("Album")
    itag = StringField()
    file_type = StringField()

class SubmitForm(FlaskForm):
    link = StringField("Link!!", validators=[DataRequired()])
    metadata = BooleanField("MetaData?", validators=[DataRequired()])
