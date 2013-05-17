import os
import inspect


num_workers = 2
backlog = 2048
daemon = False
pidfile = "/data/web/engineeringunit.com/gunicorn.pid"
debug = False
workers = 2
worker_class = 'gevent'

