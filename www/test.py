#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'LHW'

'''
orm test.
'''

import orm
from models import User, Blog, Comment

import asyncio

@asyncio.coroutine
def test(loop):
    yield from orm.create_pool(loop=loop, host='127.0.0.1', port=3306, user='www', password='www', db='awesome')

    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')

    yield from u.save()

    yield from u.remove()
    

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.stop()
