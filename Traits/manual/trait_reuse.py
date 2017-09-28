#!/usr/bin/env python

# trait_reuse.py --- Example of reusing trait definitions
from traits.api import HasTraits, Range

coefficient = Range(-1.0, 1.0, 0.0)

class quadratic(HasTraits):
    c2 = coefficient
    c1 = coefficient
    c0 = coefficient
    x  = Range(-100.0, 100.0, 0.0)

func = quadratic()
print func.c0, func.c1, func.c2
func.c0 = 0.5
func.c1 = 0.6
func.c2 = - 0.3

print func.c0, func.c1, func.c2
