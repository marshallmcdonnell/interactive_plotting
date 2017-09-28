#!/usr/bin/env python

# this.py --- Example of This predefined trait

from traits.api import HasTraits, This

class Employee(HasTraits):
    manager = This

#---------------------------------------
# Extrat
class Executive(Employee):
    pass

fred = Employee()
mary = Executive()

# The following is OK, because fred's manager can be an
# instance of Employee or any subclass.
fred.manager = mary

# This is also OK, because mary's manager can be an Employee
mary.manager = fred
