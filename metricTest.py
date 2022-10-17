
# CODE SOURCE: SOFTWARE ARCHITECTURE WITH PYTHON

"""Module metricTest.py

Metric example - Module which is used as a testbed for static
checkers.
This is a mix of different functions and classes doing
different things.
"""

import random


def fn(x, y):
    """ A function which performs a sum """
    return x + y


def find_optimal_route_to_my_office_from_home(start_time,
                                              expected_time,
                                              favorite_route='SBS1K',
                                              favorite_option='bus'):
    d = (expected_time - start_time).total_seconds()/60.0
    if d <= 30:
        return 'car'
    # If d>30 but <45, first drive then take metro
    if d > 30 and d < 45:
        return 'car', 'metro'
    if d > 45:
        return 'metro'
    # First volvo, then connecting bus
    if d < 60:
        return ('bus:335E', 'bus:connector')
    # Might as well go by normal bus
    if d > 80:
        return random.choice(('bus:330',
                              'bus:331',
                              ':'.join((favorite_option, favorite_route))))
    # Relax and choose favorite route
    elif d > 90:
        return ':'.join((favorite_option, favorite_route))


class C(object):
    """ A class which does almost nothing """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def f(self):
        pass

    def g(self, x, y):
        if self.x > x:
            return self.x + self.y
        elif x > self.x:
            return x + self.y


class D(C):
    """ D class """

    def __init__(self, x):
        self.x = x

    def f(self, x, y):
        if x > y:
            return x - y
        else:
            return x+y

    def g(self, y):
        if self.x > y:
            return self.x + y
        else:
            return y - self.x

# Testing with flake8:
# metricTest.py:2:1: E265 block comment should start with '# '
# metricTest.py:2:48: W291 trailing whitespace
# metricTest.py:13:8: E999 SyntaxError: invalid syntax
# metricTest.py:16:1: E112 expected an indented block
# metricTest.py:20:1: E128 continuation line under-indented for visual indent
# metricTest.py:21:1: E128 continuation line under-indented for visual indent
# metricTest.py:22:1: E128 continuation line under-indented for visual indent
# metricTest.py:23:1: E112 expected an indented block
# metricTest.py:27:8: E225 missing whitespace around operator
# metricTest.py:28:1: E112 expected an indented block
# metricTest.py:30:3: E261 at least two spaces before inline comment
# metricTest.py:31:8: E225 missing whitespace around operator
# metricTest.py:31:17: E225 missing whitespace around operator
# metricTest.py:32:1: E112 expected an indented block
# metricTest.py:34:3: E261 at least two spaces before inline comment
# metricTest.py:34:80: E501 line too long (83 > 79 characters)
# metricTest.py:35:2: E201 whitespace after '['
# metricTest.py:35:5: E202 whitespace before ']'
# metricTest.py:36:8: E225 missing whitespace around operator
# metricTest.py:37:1: E112 expected an indented block
# metricTest.py:37:8: E225 missing whitespace around operator
# metricTest.py:38:1: E112 expected an indented block
# metricTest.py:38:3: E261 at least two spaces before inline comment
# metricTest.py:39:22: E231 missing whitespace after ','
# metricTest.py:40:10: E225 missing whitespace around operator
# metricTest.py:41:1: E112 expected an indented block
# metricTest.py:41:3: E261 at least two spaces before inline comment
# metricTest.py:42:35: E231 missing whitespace after ','
# metricTest.py:42:45: E231 missing whitespace after ','
# metricTest.py:43:1: E128 continuation line under-indented for visual indent
# metricTest.py:44:1: E128 continuation line under-indented for visual indent
# metricTest.py:45:10: E225 missing whitespace around operator
# metricTest.py:46:1: E112 expected an indented block
# metricTest.py:46:3: E261 at least two spaces before inline comment
# metricTest.py:48:1: E128 continuation line under-indented for visual indent
# metricTest.py:52:1: E112 expected an indented block
# metricTest.py:54:24: E231 missing whitespace after ','
# metricTest.py:55:1: E112 expected an indented block
# metricTest.py:59:1: E112 expected an indented block
# metricTest.py:62:1: E112 expected an indented block
# metricTest.py:63:13: E225 missing whitespace around operator
# metricTest.py:64:1: E112 expected an indented block
# metricTest.py:65:10: E225 missing whitespace around operator
# metricTest.py:66:1: E112 expected an indented block
# metricTest.py:66:12: E225 missing whitespace around operator
# metricTest.py:69:1: E112 expected an indented block
# metricTest.py:72:1: E112 expected an indented block
# metricTest.py:74:17: E231 missing whitespace after ','
# metricTest.py:75:1: E112 expected an indented block
# metricTest.py:75:8: E225 missing whitespace around operator
# metricTest.py:76:1: E112 expected an indented block
# metricTest.py:77:8: E231 missing whitespace after ':'
# metricTest.py:78:2: E201 whitespace after '['
# metricTest.py:78:5: E202 whitespace before ']'
# metricTest.py:82:1: E112 expected an indented block
# metricTest.py:83:13: E225 missing whitespace around operator
# metricTest.py:84:1: E112 expected an indented block
# metricTest.py:86:1: E112 expected an indented block
# metricTest.py:86:19: W292 no newline at end of file
