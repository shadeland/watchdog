# -*- coding: utf-8 -*-

from handlers import base
from handlers.base import JobListHandler

url_patterns = [
    (r"/", base.MainHandler),
    (r"/job/list", JobListHandler)


]