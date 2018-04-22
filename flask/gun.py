import os
import gevent.monkey
gevent.monkey.patch_all()

import multiprocessing

debug = False
loglevel = 'error'
bind = '0.0.0.0:5000'
pidfile = 'gunicorn.pid'
logfile = 'debug.log'

#启动的进程数
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = 'gunicorn.workers.ggevent.GeventWorker'

x_forwarded_for_header = 'X-FORWARDED-FOR'