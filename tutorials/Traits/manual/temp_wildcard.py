#!/usr/bin/env python

# temp_wildcard.py --- Example of using a wildcard with a Trait
#                      attribute name
from traits.api import Any, HasTraits

class Person(HasTraits):
    temp_ = Any
