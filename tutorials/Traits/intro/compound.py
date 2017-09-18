#!/usr/bin/env python


# compound.py -- Example of multiple criteria in a trait definition
from traits.api import HasTraits, Trait, Range

class Die ( HasTraits ):

    # Define a compound trait definition:
    value = Trait( 1, Range( 1, 6 ),
                  'one', 'two', 'three', 'four', 'five', 'six' )

die = Die()
print die.value
die.value = 'five'
print die.value
