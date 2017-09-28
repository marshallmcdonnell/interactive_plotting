# -*- coding: utf-8 -*-
from __future__ import division, print_function

from traits.etsconfig.api import ETSConfig
ETSConfig.toolkit = 'qt4'
from   traits.api   import HasTraits, Instance, String
from   traitsui.api import Action, Controller, Handler, Item, View

import sys, traits, traitsui
print ('python version   :',sys.version)          # 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 08:06:12) [MSC v.1900 64 bit (AMD64)]
print ('traits version   :',traits.__version__)   # 4.6.0
print ('traitsui version :',traitsui.__version__) # 5.1.0

class Name (HasTraits):
    first = String
    last  = String
    view  = View (Item('first'), Item('last'), title='Person Name', buttons=['OK','Cancel'])
    def __str__ (self):
        return '{} {}'.format(self.first,self.last)

class Person (HasTraits):
    name = Instance(Name)

    view = View (Item('name'), title='Person Info', buttons=['OK','Cancel'])

    def __str__ (self):
        return str(self.name)


class Datastore (HasTraits):

    def add (self, person):
        print('added', person)


class PersonHandler(Handler):
    """ Handler class to add a person to a datastore.
    """
    datastore = Instance(Datastore)

    def close(self, info, is_ok):
        if is_ok:
            print('adding to datastore')
            self.datastore.add(info.object)
        else:
            print('not added')
        return super(PersonHandler, self).close(info, is_ok)
        

class Contacts (Controller):
    add  = Action (name='Add', action='_add')
    view = View (title='Datastore', buttons=[add])

    def _add (self, info):
        person = Person (name=Name())
        person.edit_traits(
            # kind='live',
            handler=PersonHandler(datastore=self.model), parent=info.ui.control
        )

datastore  = Datastore()
controller = Contacts (model=datastore)
controller.configure_traits(kind='nonmodal')
