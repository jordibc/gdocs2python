#!/usr/bin/env python

"""
Reads Python code from stdin, writes it into a file and runs it.
"""

import os
import sys
import time


doc2txt = [('\xc2\xa0', ' '),
           ('\xe2\x80\x9c', '"'),
           ('\xe2\x80\x9d', '"'),
           ('\xe2\x80\x98', "'"),
           ('\xe2\x80\x99', "'")]

while True:
    print 'Reading Python code from stdin (end with "Ctrl+d" in console):'
    try:
        code = sys.stdin.read()
    except KeyboardInterrupt:
        print '\nBye!'
        sys.exit()

    for x,y in doc2txt:
        code = code.replace(x, y)

    print '\nOverwriting "code.py" and running it...'
    open('code.py', 'w').write(code)
    t = time.time()
    os.system('python code.py')
    print ' Done (running time: %.2f s) '.center(60, '-') % (time.time() - t)
    print '\n'
