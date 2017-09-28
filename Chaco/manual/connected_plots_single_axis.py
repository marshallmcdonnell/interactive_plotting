#!/usr/bin/env python 

from numpy import linspace, sin
from traits.api import HasTraits, Instance
from traitsui.api import Item, View
from chaco.api import ArrayPlotData, Plot, HPlotContainer
from chaco.tools.api import PanTool, ZoomTool
from enable.api import ComponentEditor

class ConnectedRange(HasTraits):

    container = Instance(HPlotContainer)

    traits_view = View(Item('container', editor=ComponentEditor(),
                            show_label=False),
                       width=1000, height=600, resizable=True,
                       title="Connected Range")

    def _container_default(self):
        x = linspace(-14, 14, 100)
        y = sin(x) * x**3
        plotdata = ArrayPlotData(x = x, y = y)

        scatter = Plot(plotdata)
        scatter.plot(("x", "y"), type="scatter", color="blue")

        line = Plot(plotdata)
        line.plot(("x", "y"), type="line", color="blue")

        container = HPlotContainer(scatter, line)

        scatter.tools.append(PanTool(scatter))
        scatter.tools.append(ZoomTool(scatter))

        line.tools.append(PanTool(line))
        line.tools.append(ZoomTool(line))

        scatter.index_range = line.index_range
        return container

if __name__ == "__main__":
    ConnectedRange().configure_traits()
