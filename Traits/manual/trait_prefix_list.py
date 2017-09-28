#!/usr/bin/env python
from traits.api import HasTraits, Trait
from traits.api import TraitPrefixList
class Alien(HasTraits):
  heads = Trait('one', TraitPrefixList(['one','two','three']))

alf = Alien()
alf.heads = 'o'
print alf.heads
alf.heads = 'tw'
print alf.heads
alf.heads = 't'  # Error, not a unique prefix
