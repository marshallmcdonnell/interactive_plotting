#!/usr/bin/env python

from traits.api import HasTraits, File
from traitsui.api import FileEditor, Item, View

class FileEditorTest(HasTraits):
    filename_simple = File
    filename_custom = File
    filename_filtered = File

    view = View( Item('filename_simple', style='simple'), 
                 Item('filename_custom', style='custom'),
                 Item('filename_filtered', editor=FileEditor(filter=['*', '*.dat', '*.gr']),
                                           style='simple'),
               )

fed = FileEditorTest()
fed.configure_traits()
