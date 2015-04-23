from celery import Celery
from celery.task import periodic_task, task
from datetime import timedelta

from settings import Config
from fabric.api  import local
from uuid import uuid4
import os
celery = Celery('tasks',broker='redis://localhost:6379/2')
CFG = Config()





@task
def merge(vid,srt):
    try:

        ext =  os.path.splitext(vid)[1]

        out = 'static/uploads/%s%s' %(uuid4().hex, ext)

        result = local('ffmpeg -i %s -vf subtitles=%s -strict -2 -vcodec libx264 -b 512K -threads 4  -preset superfast  -crf 23  %s' % (vid,srt,out),capture=True)
        return out
    except Exception, e:
        print e
        return False





if __name__ == '__main__':
    merge()