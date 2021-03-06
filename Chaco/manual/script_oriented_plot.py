#!/usr/bin/env python

from numpy import linspace, pi, sin
from chaco.shell import *

x = linspace(-2*pi, 2*pi, 100)
y = sin(x)

plot(x, y, "r-")
title("First plot")
ytitle("sin(x)")
show()
