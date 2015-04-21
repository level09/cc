from uuid import uuid4
import boto
import os.path
from flask import current_app as app
from werkzeug import secure_filename
from settings import Config

CFG = Config()

def s3_upload(source_file,acl='public-read'):

    source_filename = secure_filename(source_file.filename)
    source_extension = os.path.splitext(source_filename)[1]

    destination_filename = uuid4().hex + source_extension

    print source_filename, destination_filename

    # Connect to S3
    conn = boto.connect_s3(CFG.S3_KEY, CFG.S3_SECRET)
    b = conn.get_bucket(CFG.S3_BUCKET)

    # Upload the File
    sml = b.new_key("/".join([CFG.S3_UPLOAD_DIRECTORY,destination_filename]))

    sml.set_contents_from_stream(source_file.stream())

    # Set the file's permissions.
    #sml.set_acl(acl)

    return destination_filename
