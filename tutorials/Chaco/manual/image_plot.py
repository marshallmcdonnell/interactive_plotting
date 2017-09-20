#!/usr/bin/env python 

from numpy import exp, linspace, meshgrid
from traits.api import HasTraits, Instance
from traitsui.api import Item, View
from chaco.api import ArrayPlotData, Plot, jet
from enable.api import ComponentEditor

class ImagePlot(HasTraits):
    plot = Instance(Plot)

    traits_view = View(
        Item('plot', editor=ComponentEditor(), show_label=False),
        width=500, height=500, resizable=True, title="Chaco Plot")

    def _plot_default(self):
        x = linspace(0, 10, 50)
        y = linspace(0, 5, 50)
        xgrid, ygrid = meshgrid(x, y)
        z = exp(-(xgrid*xgrid+ygrid*ygrid)/100)
        plotdata = ArrayPlotData(imagedata = z)

        plot = Plot(plotdata)
        plot.img_plot("imagedata", colormap=jet)
        return plot

if __name__ == "__main__":
    ImagePlot().configure_traits()
