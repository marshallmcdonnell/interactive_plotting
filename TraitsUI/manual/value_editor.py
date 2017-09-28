#!/usr/bin/env python

from traits.api import HasTraits
from traitsui.api import View, Item, ValueEditor

class ValueEditorTest(HasTraits):
    data = {"Name" : "Carl",
            "Date" : "today",
            "Sample" : { "Runs" : "91700-91710",
                         "Material" : "UO2",
                         "Background" : { "Runs" : "91720",
                                          "Material" : "V" },
                       }
            }

    view = View( Item(name='data', editor=ValueEditor()))

vedit = ValueEditorTest()
vedit.configure_traits()
