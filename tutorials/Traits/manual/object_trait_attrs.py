#!/usr/bin/env python

# object_trait_attrs.py --- Example of per-object trait attributes
from traits.api import HasTraits, Range

class GUISlider (HasTraits):

    def __init__(self, eval=None, label='Value',
                 trait=None, min=0.0, max=1.0,
                 initial=None, **traits):
        HasTraits.__init__(self, **traits)
        if trait is None:
            if min > max:
                min, max = max, min
            if initial is None:
                initial = min
            elif not (min <= initial <= max):
                initial = [min, max][
                            abs(initial - min) >
                            abs(initial - max)]
            trait = Range(min, max, value = initial)
        self.add_trait(label, trait)

slider = GUISlider()
slider.configure_traits()

slider = GUISlider(min=-10.0, max=10.0, initial=6.0)
slider.configure_traits()
