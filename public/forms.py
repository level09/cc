from flask_wtf import Form
from wtforms import FileField, SubmitField
from wtforms.widgets import FileInput


class VideoForm(Form):
    video = FileField('1. Choose Video', widget=FileInput())
    srt = FileField('2. Choose Subtitle (srt)', widget=FileInput())
    submit = SubmitField('Upload & Merge')