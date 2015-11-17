#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'lhw'

import asyncio
import orm

from models import User, Blog, Comment

def test(loop):
    yield from orm.create_pool(loop,user='www', password='www', db='awesome')

    u = User(name='Test4', email='test4@example.com', passwd='1234567890', image='about:blank')

    yield from u.save()

    

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
##loop.run_forever()
loop.stop
print('ok')
