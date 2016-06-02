#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Basic run script"""
from datetime import datetime

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.autoreload
from tornado.options import options
import tornado.web
import motor.motor_tornado
from apscheduler.schedulers.tornado import TornadoScheduler
from lib.job import JobCreator


from settings import settings
from urls import url_patterns







import logging
FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s]"
logging.basicConfig(level=logging.DEBUG, format=FORMAT)




class TornadoApplication(tornado.web.Application):

    def __init__(self):
        tornado.web.Application.__init__(self, url_patterns, **settings)

# Test Handler to add and delete jobs

def tick():
    print('Tick! The time is %s' % datetime.now())


def main():
    # Running APScheduler
    aps = TornadoScheduler()
    aps.add_jobstore('mongodb', collection='url_jobs')
    aps.start()
    aps.remove_all_jobs()
    db_client = motor.motor_tornado.MotorClient()
    jc = JobCreator()
    jc.create_job("google.com", "1111", aps, db_client)

    # Running server
    app = TornadoApplication()
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
