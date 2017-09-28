#!/usr/bin/env python

# traitprefixmap.py --- Example of using the TraitPrefixMap handler
from traits.api import Trait, TraitPrefixMap, HasTraits

boolean_map = Trait('true', TraitPrefixMap( {
                              'true': 1,
                              'yes':  1,
                              'false': 0,
                              'no':   0 } ) )

class Inputter(HasTraits):
    option = boolean_map

myInput = Inputter()
print myInput.option, myInput.option_
