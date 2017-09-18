#!/usr/bin/env python

# custom_traithandler.py --- Example of a custom TraitHandler
import types
from traits.api import TraitHandler

class TraitOddInteger(TraitHandler):
    def validate(self, object, name, value):
        if ((type(value) is types.IntType) and
            (value > 0) and ((value % 2) == 1)):
            return value
        self.error(object, name, value)

    def info(self):
        return '**a positive odd integer**'
