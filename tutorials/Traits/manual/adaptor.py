#!/usr/bin/env python

from traits.api import Adapter, Instance, provides, register_factory
from interface import IName, Person

# Declare what interfaces this adapter implements for its client
@provides(IName)
class PersonToIName(Adapter):

    # Declare the type of client it supports:
    adaptee = Instance(Person)

    # Implement the 'IName' interface on behalf of its client:
    def get_name ( self ):
        name = '{first} {last}'.format(first=self.adaptee.first_name,
                                       last=self.adaptee.last_name)
        return name


# ... somewhere else at application startup.
register_factory(PersonToIName, Person, IName)
