#!/usr/bin/env python

from traits.api import HasTraits, List, Str
from traitsui.api import View, Item, ListEditor


class ListEditorTest(HasTraits):
    my_simple_list = List(Str, ['Cat', 'Dog'])

    view = View( Item(name='my_simple_list', editor=ListEditor(use_notebook=True)),
               )


my_list = ['Sample', 'BackRun', 'NormRun', 'EmptyEnv', 'EmtpyInstr']

#list_ed = ListEditorTest(my_simple_list = my_list)
list_ed = ListEditorTest()
list_ed.configure_traits()
