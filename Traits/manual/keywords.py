#!/usr/bin/env python

# keywords.py --- Example of trait keywords
from traits.api import HasTraits, Str

class Person(HasTraits):
    first_name = Str('',
                     desc='first or personal name',
                     label='First Name')
    last_name =  Str('',
                     desc='last or family name',
                     label='Last Name')
