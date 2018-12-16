# from future import absolute_import
from celery import Celery
import time
app = Celery('tasks',
                    broker='redis://localhost',
                    backend='redis://localhost'

)

@app.task
def add(x, y): # 这是worker可以执行的一个任务
    print("runing...{}+{}".format(x,y))
    return x+y

@app.task
def cmd(cmd_str):
    print("running {}...".format(cmd_str))
    time.sleep(10)
    return time.time()


