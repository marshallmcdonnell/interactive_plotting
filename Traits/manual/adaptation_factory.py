#!/usr/bin/env python

import abc
import numpy
from traits.api import Array, HasTraits
from traits.adaptation.api import adapt, Adapter, register_factory

class ImageABC(object):
    __metaclass__ = abc.ABCMeta

class NDArrayToImage(Adapter):
    adaptee = Array

# Declare that NDArrayToImage implements ImageABC.
ImageABC.register(NDArrayToImage)


def ndarray_to_image_abc(adaptee):
    """ An adapter factory from numpy arrays to the ImageABC protocol."""
    if adaptee.ndim == 2:
        return NDArrayToImage(adaptee=adaptee)
    return None

# ... somewhere else at application startup
register_factory(ndarray_to_image_abc, numpy.ndarray, ImageABC)

# Try to adapt numpy arrays to images. The `adapt` function is
# introduced later in the docs, but you can probably guess what it does ;-)

# This adaptation fails, as the array is 1D
image = adapt(numpy.ndarray([1,2,3]), ImageABC, default=None)
assert image == None

# This succeeds.
image = adapt(numpy.array([[1,2],[3,4]]), ImageABC)
assert isinstance(image, NDArrayToImage)
