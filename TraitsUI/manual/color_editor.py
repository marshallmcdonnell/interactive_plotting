#!/usr/bin/env python

from traits.api import HasTraits, Color
from traitsui.api import View, Item, ColorEditor

class ColorEditorTest(HasTraits):

    color_simple   = Color
    color_mapped   = Color
    color_custom   = Color
    color_text     = Color
    color_readonly = Color

    view = View( Item('color_simple', style='simple'),
                 Item('color_mapped', editor=ColorEditor(mapped=True)),
                 Item('color_custom', style='custom'),
                 Item('color_text', style='text'),
                 Item('color_readonly', style='readonly'),
               )


color_test = ColorEditorTest()
color_test.configure_traits()
