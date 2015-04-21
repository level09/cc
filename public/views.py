from flask import Flask, request, abort, Response, redirect, url_for, flash, Blueprint, send_from_directory
from flask.templating import render_template
from flask_security.decorators import roles_required, login_required
from public.forms import VideoForm

from settings import Config
from tools import s3_upload
import os
bp_public = Blueprint('public',__name__, static_folder='../static')


@bp_public.route('/')
def index():
    return render_template('index.html',form = VideoForm())


@bp_public.route('/robots.txt')
def static_from_root():
    return send_from_directory(bp_public.static_folder, request.path[1:])



@bp_public.route('/submit',methods=['POST'])
def submit():

    form = VideoForm(request.form)

    if form.validate_on_submit():

        output = s3_upload(request.files['video'])
        print output



    return 'done'