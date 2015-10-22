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

    for user in (yield from User.findAll()):
        yield from user.remove()

    u = User(name='Test1', email='test1@example.com', passwd='1234567890', image='about:blank')

    yield from u.save()

    u = User(name='Test2', email='test2@example.com', passwd='1234567890', image='about:blank')

    yield from u.save()

    for user in (yield from User.findAll('name=\'Test2\'')):
        print (user)

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.stop()
