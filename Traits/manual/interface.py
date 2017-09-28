#!/usr/bin/env python

from traits.api import HasTraits, Interface, provides, Str, Instance

class IName(Interface):
    def get_name(self):
        """ Returns a string which is the name of an object. """

@provides(IName)
class Person(HasTraits):

    first_name = Str( 'John' )
    last_name  = Str( 'Doe' )

    # Implementation of the 'IName' interface:
    def get_name ( self ):
        ''' Returns the name of an object. '''
        name = '{first} {last}'
        return name.format(first=self.first_name, last=self.last_name)

person = Person()
person.first_name = "Bill"
person.last_name = "Johnson"

print person.get_name()


class Apartment(HasTraits):
    renter = Instance(IName)
william = Person(first_name='William', last_name='Adams')
apt1 = Apartment( renter=william )
print 'Renter is: ', apt1.renter.get_name()
