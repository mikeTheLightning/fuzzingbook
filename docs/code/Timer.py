#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This material is part of "Generating Software Tests".
# Web site: https://www.fuzzingbook.org/html/Timer.html
# Last change: 2018-10-08 08:15:45-07:00
#
#
# Copyright (c) 2018 Saarland University, CISPA, authors, and contributors
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


# # Timer

if __name__ == "__main__":
    print('# Timer')




# ## Measuring Time

if __name__ == "__main__":
    print('\n## Measuring Time')




if __name__ == "__main__":
    # We use the same fixed seed as the notebook to ensure consistency
    from fuzzingbook_utils import set_fixed_seed
    set_fixed_seed.set_fixed_seed()



import time

def clock():
    try:
        return time.perf_counter()  # Python 3
    except:
        return time.clock()         # Python 2

class Timer(object):
    # Begin of `with` block
    def __enter__(self):
        self.start_time = clock()
        self.end_time = None
        return self

    # End of `with` block
    def __exit__(self, exc_type, exc_value, tb):
        self.end_time = clock()

    def elapsed_time(self):
        """Return elapsed time in seconds"""
        if self.end_time is None:
            # still running
            return clock() - self.start_time
        else:
            return self.end_time - self.start_time

def some_long_running_function():
    i = 1000000
    while i > 0:
        i -= 1

if __name__ == "__main__":
    print("Stopping total time:")
    with Timer() as t:
        some_long_running_function()
    print(t.elapsed_time())


if __name__ == "__main__":
    print("Stopping time in between:")
    with Timer() as t:
        for i in range(10):
            print(t.elapsed_time())

