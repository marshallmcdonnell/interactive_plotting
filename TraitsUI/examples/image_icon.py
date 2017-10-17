#!/usr/bin/env python

from traits.api import HasTraits, Str
from traitsui.api import View, Item
from pyface.image_resource import ImageResource

class Person(HasTraits):
    first_name = Str
    last_name = Str

    view = View(Item('first_name'),
             Item('last_name'),
             icon=ImageResource('./equation_example.png')
            )

Person().configure_traits()
