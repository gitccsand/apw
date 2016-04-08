#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Default configurations.
'''

__author__ = 'Liu Hongwei'

configs = {
    'debug': True,
    'db': {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'zichan',
        'password': 'zichan901',
        'db': 'asset'
    },
    'session': {
        'secret': 'Asset'
    }
}
