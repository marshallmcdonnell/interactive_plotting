#!/usr/bin/env python 

from traits.api import HasTraits, Int

class Curmudgeon(HasTraits):
    constant = Int(1)
    def _constant_changed(self):
        raise ValueError()

c = Curmudgeon()
c.constant = 42
