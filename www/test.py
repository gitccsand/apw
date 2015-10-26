#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'LHW'

'''
orm test.
'''

import orm
from models import User, Blog, Comment

import asyncio
import logging

@asyncio.coroutine
def test(loop):
    yield from orm.create_pool(loop=loop, host='127.0.0.1', port=3306, user='www', password='www', db='awesome')

    for user in (yield from User.findAll()):
        yield from user.remove()

    u = User(name='Test1', email='test1@example.com', passwd='1234567890', image='about:blank')

    yield from u.save()

    u = User(name='Test2', email='test2@example.com', passwd='1234567890', image='about:blank',ddd='ddd')

    yield from u.save()

    u = User(name='Test3',  passwd='1234567890', image='about:blank')
    try:
        yield from u.save()
    except BaseException as e:
        logging.error('USER Insert Sql error:',e)

    name='kk\' or \'password\'=\'password'
##    name='Test1'
    where='name=\''+name+'\''
    print(where)
    try:
        for user in (yield from User.findAll(where)):
            print (user)
    except BaseException as e:
        logging.ERROR(e)
            

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.stop()
