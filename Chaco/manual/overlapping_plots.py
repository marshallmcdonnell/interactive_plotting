#!/usr/bin/env python 

from numpy import cos, linspace, sin
from traits.api import HasTraits, Instance
from traitsui.api import Item, View
from chaco.api import ArrayPlotData, Plot
from enable.api import ComponentEditor

class OverlappingPlot(HasTraits):

    plot = Instance(Plot)

    traits_view = View(
        Item('plot',editor=ComponentEditor(), show_label=False),
        width=500, height=500, resizable=True, title="Chaco Plot")

    def _plot_default(self):
        x = linspace(-14, 14, 100)
        y = x/2 * sin(x)
        y2 = cos(x)
        plotdata = ArrayPlotData(x=x, y=y, y2=y2)

        plot = Plot(plotdata)
        plot.plot(("x", "y"), type="scatter", color="blue")
        plot.plot(("x", "y2"), type="line", color="red")
        return plot

if __name__ == "__main__":
    OverlappingPlot().configure_traits()
