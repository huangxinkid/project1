from __future__ import absolute_import, unicode_literals
from celery import Celery


app = Celery('proj',                         # app的名字
             broker='redis://localhost', 
             backend='redis://localhost',
             include=['s3proj.tasks', 's3proj.tasks2'])	    #存任务的文件

# app.conf.update(
#             result_expires=3600,
#             )

if __name__ == '__main__':
    app.start()

	
