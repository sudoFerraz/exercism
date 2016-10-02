#
# Skeleton file for the Python "Hello World" exercise.
#
# -*- coding: latin-1 -*-
#!/usr/bin/env python

import sys


def hello(name=''):
    if name == '' or name == None:
        name = 'World'
    doido = 'Hello, %s!' % name
    return doido

