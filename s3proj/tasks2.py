from __future__ import absolute_import, unicode_literals
from .celery import app


@app.task
def cmd(cmdstr):
    print('running cmd ...{}'.format(cmdstr))

@app.task
def file_transfer(filename):
    print("sending file...{}".format(filename))