#!/usr/bin/env python 

# mapped.py --- Example of a mapped trait
from traits.api import HasTraits, Trait

standard_color = Trait ('black',
              {'black':       (0.0, 0.0, 0.0, 1.0),
               'blue':        (0.0, 0.0, 1.0, 1.0),
               'cyan':        (0.0, 1.0, 1.0, 1.0),
               'green':       (0.0, 1.0, 0.0, 1.0),
               'magenta':     (1.0, 0.0, 1.0, 1.0),
               'orange':      (0.8, 0.196, 0.196, 1.0),
               'purple':      (0.69, 0.0, 1.0, 1.0),
               'red':         (1.0, 0.0, 0.0, 1.0),
               'violet':      (0.31, 0.184, 0.31, 1.0),
               'yellow':      (1.0, 1.0, 0.0, 1.0),
               'white':       (1.0, 1.0, 1.0, 1.0),
               'transparent': (1.0, 1.0, 1.0, 0.0) } )

red_color = Trait ('red', standard_color)

class GraphicShape (HasTraits):
    line_color = standard_color
    fill_color = red_color

my_shape1 = GraphicShape()
print my_shape1.line_color, my_shape1.fill_color
print my_shape1.line_color_, my_shape1.fill_color_
my_shape2 = GraphicShape()
my_shape2.line_color = 'blue'
my_shape2.fill_color = 'green'
print my_shape2.line_color, my_shape2.fill_color
print my_shape2.line_color_, my_shape2.fill_color_
