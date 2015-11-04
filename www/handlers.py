#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Michael Liao'

' url handlers '

import coroweb
import models
@coroweb.get('/')
def index():
    users = (yield from models.User.findAll())
    return {
        '__template__' : 'test.html',
        'users' : users
        }
