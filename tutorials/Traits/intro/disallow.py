#!/usr/bin/env python

# disallow.py --- Example of using Disallow with wildcards
from traits.api import \
    Disallow, Float, HasTraits, Int, Str

class Person (HasTraits):
    name   = Str
    age    = Int
    weight = Float
    _      = Disallow
