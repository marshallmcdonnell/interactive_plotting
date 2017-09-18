#!/usr/bin/env python

# delegate.py --- Example of trait delegation
from traits.api \
    import DelegatesTo, HasTraits, Instance, Str

class Parent(HasTraits):
    first_name = Str
    last_name  = Str

class Child(HasTraits):
    first_name = Str
    last_name  = DelegatesTo('father')
    father     = Instance(Parent)
    mother     = Instance(Parent)

tony  = Parent(first_name='Anthony', last_name='Jones')
alice = Parent(first_name='Alice', last_name='Smith')
sally = Child( first_name='Sally', father=tony, mother=alice)
print sally.last_name
sally.last_name = 'Cooper' # Updates delegatee
print tony.last_name
sally.last_name = sally.mother # ERR: string expected
