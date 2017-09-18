#!/usr/bin/env python

from traits.api import *
from traits.util.event_tracer import record_events


class MyModel(HasTraits):

    number = Float(2.0)
    list_of_numbers = List(Float())
    count = Int(0)

    @on_trait_change('number')
    def _add_number_to_list(self, value):
        self.list_of_numbers.append(value)

    @on_trait_change('list_of_numbers[]')
    def _count_items(self):
        self.count = len(self.list_of_numbers)

    def add_to_number(self, value):
        self.number += value


my_model = MyModel()

with record_events() as change_event_container:
    my_model.number = 4.7
    my_model.number = 3

# save files locally
print "Change to Events found in file: MainThread.trace"
change_event_container.save_to_directory('./')
