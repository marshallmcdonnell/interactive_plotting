#!/usr/bin/env python

from numpy import linspace, sin
from traits.api import HasTraits, Instance
from traitsui.api import Item, View
from chaco.api import ArrayPlotData, Plot
from enable.api import ComponentEditor

class ScatterPlot(HasTraits):
    plot = Instance(Plot)

    traits_view = View(
        Item('plot',editor=ComponentEditor(), show_label=False),
        width=500, height=500, resizable=True, title="Chaco Plot")

    def _plot_default(self):
        x = linspace(-14, 14, 100)
        y = sin(x) * x**3
        plotdata = ArrayPlotData(x = x, y = y)

        plot = Plot(plotdata)
        plot.plot(("x", "y"), type="scatter", color="blue")
        plot.title = "sin(x) * x^3"
        return plot

if __name__ == "__main__":
    ScatterPlot().configure_traits()
