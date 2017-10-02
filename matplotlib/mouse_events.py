#!/usr/bin/env python
from __future__ import print_function

import matplotlib
#matplotlib.use("WxAgg")
#matplotlib.use("TkAgg")
#matplotlib.use("GTKAgg")
#matplotlib.use("Qt4Agg")
#matplotlib.use("MacOSX")
import matplotlib.pyplot as plt

#print("***** TESTING WITH BACKEND: %s"%matplotlib.get_backend() + " *****")


def OnClick(event):
    if event.dblclick:
        print("DBLCLICK", event)
    elif event.button == 0:
        print("0 ", event)
    elif event.button == 1:
        print("1 ", event)
    elif event.button == 2:
        print("2 ", event)
    elif event.button == 3:
        print("3 ", event)
    elif event.button == 'up':
        print("UP ", event)
    elif event.button == 'down':
        print("down ", event)
    elif event.button == None:
        print("None ", event)
    else:
        print("? ", event)
        


def OnRelease(event):
    print("UP      ", event)


fig = plt.gcf()
cid_up = fig.canvas.mpl_connect('button_press_event', OnClick)
cid_down = fig.canvas.mpl_connect('button_release_event', OnRelease)

plt.gca().text(0.5, 0.5, "Click on the canvas to test mouse events.",
               ha="center", va="center")

plt.show()
