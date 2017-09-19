#!/usr/bin/env python

# bad_self_ref.py --- Non-working example with self- referencing
#                     class definition
from traits.api import HasTraits, Instance
class Employee(HasTraits):
    manager = Instance(Employee)
