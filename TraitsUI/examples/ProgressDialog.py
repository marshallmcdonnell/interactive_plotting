#!/usr/bin/env python

import time
from pyface.api import ProgressDialog

def task_func(t):
    progress = ProgressDialog(title="progress", 
                              message="counting to %d" % t,
                              max=t, 
                              show_time=True, 
                              can_cancel=True)
    progress.open()

    for i in range(0,t+1):
        time.sleep(1)
        #print i
        (cont, skip) = progress.update(i)
        if not cont or skip:
            break

        progress.update(i)


task_func(100)
