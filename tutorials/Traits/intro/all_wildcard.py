#!/usr/bin/env python

# all_wildcard.py --- Example of trait attribute wildcard rules
from traits.api import Any, HasTraits, Int, Str

class Person ( HasTraits ):

    # Normal, explicitly defined trait:
    name = Str

    # By default, let all traits have any value:
    _ = Any

    # Except for this one, which must be an Int:
    age = Int
bill = Person()
# These assignments should all work:
bill.name      = 'William'
bill.address  = '121 Drury Lane'
bill.zip_code = 55212
bill.age      = 49
# This should generate an error (must be an Int):
bill.age = 'middle age' # ERR: age must be TraitType Int
