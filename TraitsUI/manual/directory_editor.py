#!/usr/bin/env python

from traits.api import HasTraits, Directory
from traitsui.api import View, Item, DirectoryEditor

class DirectoryEditorTest(HasTraits):

    directory_simple   = Directory
    directory_custom   = Directory

    view = View( Item('directory_simple', style='simple'),
                 Item('directory_custom', style='custom'),
               )


directory_test = DirectoryEditorTest()
directory_test.configure_traits()
