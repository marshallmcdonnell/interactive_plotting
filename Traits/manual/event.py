#!/usr/bin/env python

# event.py --- Example of trait event
from traits.api import Event, HasTraits, List, Tuple, RGBColor

point_2d = Tuple(0, 0)


class Line2D(HasTraits):
    points = List(point_2d)
    line_color = RGBColor('black')
    updated = Event

    def redraw(self):
        print "Redrawn"

    def _points_changed(self):
        self.updated = True

    def _updated_fired(self):
        self.redraw()


print "Initializing line..."
line = Line2D()
print "Adding points to line..."
line.points = [ (0, 0), (1, 2), ]
print "Adding another point to the line..."
line.points.append( (3,4) )

class DynamicLine2D(HasTraits):
    points = List(point_2d)
    line_color = RGBColor('black')
    
    def initialize(self):
        print "Initialized"

    def redraw(self):
        print "Redrawn"

    def _points_changed(self):
        self.initialize()

    def _points_items_changed(self):
        self.redraw()


print "---Dynamic---"
print "Initializing line..."
line = DynamicLine2D()
print "Adding points to line..."
line.points = [ (0, 0), (1, 2), ]
print "Adding another point to the line..."
line.points.append( (3,4) )
print "Adding another point to the line..."
line.points.append( (4,5) )

