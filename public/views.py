from flask import Flask, request, abort, Response, redirect, url_for, flash, Blueprint, send_from_directory
from flask.templating import render_template
from flask_security.decorators import roles_required, login_required
from public.forms import VideoForm
from werkzeug import secure_filename
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
    if request.method == 'POST':

        video = request.files['video'] if 'video' in request.files else None
        srt = request.files['srt'] if 'srt' in request.files else None
        vid_name = None
        srt_name = None

        if video:
            vid_name = secure_filename(video.filename)
            video.save(os.path.join(Config().UPLOAD_DIR,  vid_name))
        if srt:
            srt_name = secure_filename(srt.filename)
            srt.save(os.path.join(Config().UPLOAD_DIR,srt_name))



    return 'done'