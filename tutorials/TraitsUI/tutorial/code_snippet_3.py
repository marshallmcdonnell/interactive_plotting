#!/usr/bin/env python
from traits.api import *
import wx

class Counter(HasTraits):
    value = Int()

counter = Counter()
counter.edit_traits()
counter.configure_traits()
