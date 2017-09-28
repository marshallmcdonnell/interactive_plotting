#!/usr/bin/env python

# use_custom_th.py --- Example of using a custom TraitHandler
from traits.api import HasTraits, Trait, TraitRange
from custom_traithandler import TraitOddInteger

class AnOddClass(HasTraits):
    oddball = Trait(1, TraitOddInteger())
    very_odd = Trait(-1, TraitOddInteger(),
                         TraitRange(-10, -1))

odd_stuff = AnOddClass()
odd_stuff.very_odd = 0 # ERR: Gives verbose error from info() in TraitOddInteger
