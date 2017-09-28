#!/usr/bin/env python 

# configure_traits.py -- Sample code to demonstrate
#                        configure_traits()
from traits.api import HasTraits, Str, Int
import traitsui

class SimpleEmployee(HasTraits):
    first_name = Str
    last_name = Str
    department = Str

    employee_number = Str
    salary = Int

sam = SimpleEmployee()
sam.configure_traits()
