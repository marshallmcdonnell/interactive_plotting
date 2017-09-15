#!/usr/bin/env python

from traits.api import *
from traitsui.api import *


class Camera(HasTraits):
    """ Camera object """
    gain = Enum( 1, 2, 3,
                 desc="The gain index of the camera",
                 label="Gain", )

    exposure = CInt( 10, 
                     desc="The exposure time, in ms",
                     label="Exposure", )
    
    def capture(self):
        """ Captures an image on the camera and returns it """
        print("Capturing an image at %i ms exposure, gain: %i" % (self.exposure, self.gain))


if __name__ == "__main__":
    camera = Camera()
    camera.configure_traits()
    camera.capture()
