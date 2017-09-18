#!/usr/bin/env python
from traits.api import Enum, HasTraits, List
class InventoryItem(HasTraits):
   possible_stock_states = List([None, 0, 1, 2, 3, 'many'])
   stock = Enum(0, values="possible_stock_states")
           # Enumerated list, default value is 0. The list of
           # allowed values is whatever possible_stock_states holds


hats = InventoryItem()
hats.stock
hats.stock = None
hats.stock = 2      # OK
#hats.stock = 4      # TraitError like above

hats.possible_stock_states.append(4)  # Add 4 to list of allowed values
hats.stock = 4      # OK
hats.stock = 'many'


class AbsCorrection(HasTraits):
    possible_absorption_correction_types = List([None, 'Mayers', 'CarpenterInPlane', 'PaalmanPings', 'Soper'])
    correction = Enum('', values="possible_absorption_correction_types")

abscorr = AbsCorrection()
print(abscorr.correction)
abscorr.correction = 'Soper'
print(abscorr.correction)
abscorr.possible_absorption_correction_types.append('CarpenterOutOfPlane')
abscorr.correction = 'CarpenterOutOfPlane'
print(abscorr.correction)
