#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""

"""
__author__ = "Curry"

import base64

a = 'this is a test'
b = base64.urlsafe_b64encode(a.encode('utf-8'))
print(b)
d = b.decode('utf-8')
print(d)
d = [('name', 'curry'), ('age', '10')]
d1 = dict(d)
print(d1)
