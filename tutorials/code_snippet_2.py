#!/usr/bin/env python

from traits.api import *
from traitsui.api import *


class Camera(HasTraits):
    """ Camera object """
    gain = Enum( 1, 2, 3,)

    exposure = CInt( 10, label="Exposure", )

class TextDisplay(HasTraits):
    string = String()
    view = View( Item('string', show_label=False, springy=True, style='custom') )

class Container(HasTraits):
    camera = Instance(Camera)
    display = Instance(TextDisplay)
    
    view = View(
                 Item('camera', style='custom', show_label=False, ),
                 Item('display', style='custom', show_label=False,),
               )
    

if __name__ == "__main__":

    container = Container(camera=Camera(), display=TextDisplay())
    container.configure_traits()
