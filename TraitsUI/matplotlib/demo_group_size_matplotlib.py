"""
Control the height and width of a Group

TraitsUI does not permit explicit specification of the height or width of a
Group (or its descendants). The workaround is to put each Group whose size you
wish to control into its own View class, which can be an Item (hence can be
size-controlled) in the larger View. Sometimes it is necessary to repeat such
surgery at several levels to get the desired layout.

We separate the left and right groups by a splitter (HSplit), and also
make the window itself resizable.

This demo has the Chaco stuff "ripped out" and replaced by Matplotlib

"""
#--------------------------------------------------------------------------#
# TraitsUI imports

from numpy import linspace, pi, sin
from traits.api import HasTraits, Instance, Str, Float, Int, Array, on_trait_change
# UItem is Unlabeled Item
from traitsui.api import View, Item, UItem, HSplit, InstanceEditor, \
    VGroup, HGroup

#--------------------------------------------------------------------------#
# Matplotlib Imports

import matplotlib
# We want matplotlib to use a QT backend
matplotlib.use('Qt4Agg')
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from traits.api import Any, Instance
from traitsui.qt4.editor import Editor
from traitsui.qt4.basic_editor_factory import BasicEditorFactory

#--------------------------------------------------------------------------#
# Matplotlib Additions

class _MPLFigureEditor(Editor):

   scrollable  = True

   def init(self, parent):
       self.control = self._create_canvas(parent)
       self.set_tooltip()

   def update_editor(self):
       pass

   def _create_canvas(self, parent):
       """ Create the MPL canvas. """
       # matplotlib commands to create a canvas
       mpl_canvas = FigureCanvas(self.value)
       return mpl_canvas

class MPLFigureEditor(BasicEditorFactory):

   klass = _MPLFigureEditor


#--------------------------------------------------------------------------#
# Main TraitsUI section

class PlotView(HasTraits):
    """Defines a sub-view whose size we wish to explicitly control."""
    scale = Float(1.0)
    xdata = Array
    ydata = Array
    figure = Instance(Figure, ())

    view = View(
        # This HGroup keeps 'n' from over-widening, by implicitly placing
        # a spring to the right of the item.
        HGroup(Item('scale')),
        UItem('figure', editor=MPLFigureEditor()),
        resizable=True,
    )


    @on_trait_change('xdata,ydata,scale')
    def plot(self):
        x = self.xdata
        y = self.ydata

        if len(x) != len(y): return

        print self.figure
        print self.figure.axes
        if len(self.figure.axes) == 0:
            axes = self.figure.add_subplot(111)
 
        axes = self.figure.axes[0]

        if not axes.lines:
            axes.plot(x,self.scale*y)
        else:
            l = axes.lines[0]
            l.set_xdata(x)
            l.set_ydata(self.scale*y)
        canvas = self.figure.canvas
        if canvas is not None:
          canvas.draw()



class VerticalBar(HasTraits):
    """Defines a sub-view whose size we wish to explicitly control."""
    string = Str('abcdefg')
    shift = Float('0.0')
    view = View(
        VGroup(
            Item('string'),
            Item('shift'),
            show_border=True,
        ),
    )


class BigView(HasTraits):
    """Defines the top-level view. It contains two side-by-side panels (a
    vertical bar and a plot under an integer) whose relative sizes we wish
    to control explicitly. If these were simply defined as Groups, we could
    not control their sizes. But by extracting them as separate classes with
    their own views, the resizing becomes possible, because they are loaded
    as Items now.
    """
    bar = Instance(VerticalBar, ())
    plot = Instance(PlotView)

    view = View(
        HSplit(
            # Specify pixel width of each sub-view. (Or, to specify
            # proportionate width, use a width < 1.0)
            # We specify the height here for sake of demonstration;
            # it could also be specified for the top-level view.
            UItem('bar', width=150,style='custom',editor=InstanceEditor() ),
            UItem('plot', width=500, height=500,style='custom',editor=InstanceEditor() ),
            show_border=True,
        ),
        resizable=True,
    )

    @on_trait_change('bar.shift')
    def shift_plot(self):
        self.plot.ydata = self.plot.ydata + self.bar.shift

    @on_trait_change('bar.string')
    def print_string(self):
        print self.bar.string

x = linspace(-2 * pi, 2 * pi, 100)
pv = PlotView(xdata=x, ydata=sin(x))
bv = BigView(plot=pv)
bv.configure_traits()

