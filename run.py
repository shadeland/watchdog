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
from apscheduler.schedulers.tornado import TornadoScheduler


from settings import settings
from urls import url_patterns
import logging
logging.basicConfig(level=logging.DEBUG)


class TornadoApplication(tornado.web.Application):

    def __init__(self):
        tornado.web.Application.__init__(self, url_patterns, **settings)


def tick():
    print('Tick! The time is %s' % datetime.now())


def main():
    # Running APScheduler
    aps = TornadoScheduler()
    aps.add_jobstore('mongodb', collection='url_jobs')
    aps.start()
    # Running server

    app = TornadoApplication()
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
