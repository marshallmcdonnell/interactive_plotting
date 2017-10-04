#!/usr/bin/env python

from traits.api import *
from traitsui.api import *
from PyQt4 import QtCore, QtGui



class HouseHandler(Handler):

    def object_pool_changed(self,info):
        if info.object.pool:
            print info.ui.control
            print info.ui.control.children()
            qtObject = info.ui.control
            palette = qtObject.palette()
            qtObject.setAutoFillBackground(True)
            #palette.setColor(qtObject.backgroundRole(), QtCore.Qt.red)
            #qtObject.setPalette(palette)
            #or with style sheets
            info.ui.control.setStyleSheet('background-color: red')
        else:
            info.ui.control.setStyleSheet('background-color: None')


class House(HasTraits):
    address = Str
    bedrooms = Int
    pool = Bool
    price = Int
    traits_view =View(
            Group(Item('address', style="readonly"), Item('bedrooms'), Item('pool'), Item('price'),show_border=True),
            handler = HouseHandler()
        )

hs = House()
hs.configure_traits()
