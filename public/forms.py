from flask_wtf import Form
from wtforms import FileField, SubmitField
from wtforms.widgets import FileInput


class VideoForm(Form):
    video = FileField('Video', widget=FileInput())
    srt = FileField('Subtitle (srt)', widget=FileInput())
    submit = SubmitField('Upload & Merge')