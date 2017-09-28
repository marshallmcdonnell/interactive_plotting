#!/usr/bin/env python

# wildcard_rules.py -- Example of trait attribute wildcard rules
from traits.api import Any, HasTraits, Int, Python

class Person(HasTraits):
    temp_count = Int(-1)
    temp_      = Any
    _          = Python
