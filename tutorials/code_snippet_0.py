#!/usr/bin/env python
from __future__ import (absolute_import, division, print_function)
import numpy as np

class Point(object):
    """ 3D Print objects"""
    x = 0.
    y = 0.
    z = 0.

    def rotate_z(self, theta):
        """ rotate the point around the Z axis"""
        xtemp =  np.cos(theta) * self.x + np.sin(theta) * self.y
        ytemp = -np.sin(theta) * self.x + np.cos(theta) * self.y
        self.x = xtemp
        self.y = ytemp

class ColoredPoint(Point):
    """ Colored 3D print """
    color = "white"

if __name__ == "__main__":
    p = Point()
    p.x = 1
    print(p.x, p.y, p.z)
    p.rotate_z(np.pi)
    print(p.x, p.y, p.z)

    cp = ColoredPoint()
    cp.x = 1
    print(cp.x, cp.y, cp.z, cp.color)
    cp.rotate_z(np.pi/2.)
    print(cp.x, cp.y, cp.z, cp.color)
