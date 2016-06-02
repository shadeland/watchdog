# -*- coding: utf-8 -*-

from handlers import base
from handlers.base import JobListHandler, JobHandler

url_patterns = [
    (r"/", base.MainHandler),
    (r"/job/list", JobListHandler),
    (r"/job", JobHandler)


]