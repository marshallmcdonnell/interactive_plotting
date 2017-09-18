#!/usr/bin/env python

# deferring_notification.py -- Example of notification with deferring
from traits.api \
    import HasTraits, Instance, PrototypedFrom, Str

class Parent ( HasTraits ):

    first_name = Str
    last_name  = Str

    def _last_name_changed(self, new):
        print "Parent's last name changed to %s." % new

class Child ( HasTraits ):

    father = Instance( Parent )
    first_name = Str
    last_name  = PrototypedFrom( 'father' )

    def _last_name_changed(self, new):
        print "Child's last name changed to %s." % new

dad = Parent( first_name='William', last_name='Chase' )
son = Child( first_name='John', father=dad )
dad.last_name='Jones'
son.last_name='Thomas'
dad.last_name='Riley'
print "Deleting son's last_name (makes link re-establish to father)"
del son.last_name
dad.last_name='Simmons'
