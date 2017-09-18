#!/usr/bin/env python


# static_notification.py --- Example of static attribute
#                            notification
from traits.api import HasTraits, Float

class Person(HasTraits):
    weight_kg = Float(0.0)
    height_m =  Float(1.0)
    bmi = Float(0.0)

    def _weight_kg_changed(self, old, new):
         print 'weight_kg changed from %s to %s ' % (old, new)
         if self.height_m != 0.0:
             self.bmi = self.weight_kg / (self.height_m**2)

    def _anytrait_changed(self, name, old, new):
         print 'The %s trait changed from %s to %s ' \
                % (name, old, new)

bob = Person()
bob.height_m = 1.75
bob.weight_kg = 100.0

