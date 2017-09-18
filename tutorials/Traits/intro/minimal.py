#!/usr/bin/env python 

# minimal.py --- Minimal example of using traits.

from traits.api import HasTraits, Float

class Person(HasTraits):
    weight = Float(150.0)
