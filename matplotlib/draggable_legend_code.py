#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as _plt


class DraggableLegend:
    def __init__(self, legend):
        self.legend = legend
        self.gotLegend = False
        legend.figure.canvas.mpl_connect('motion_notify_event', self.on_motion)
        legend.figure.canvas.mpl_connect('pick_event', self.on_picker)
        legend.figure.canvas.mpl_connect('button_release_event', self.on_release)
        legend.set_picker(self.my_legend_picker)


    #----------------------------------------------------#
    # Connected event handlers

    def on_motion(self, event):
        if self.gotLegend:
            dx = event.x - self.mouse_x
            dy = event.y - self.mouse_y
            loc_in_canvas = self.legend_x + dx, self.legend_y + dy
            loc_in_norm_axes = self.legend.parent.transAxes.inverted().transform_point(loc_in_canvas)
            self.legend._loc = tuple(loc_in_norm_axes)
            self.legend.figure.canvas.draw()

    def my_legend_picker(self, legend, event): 
        return self.legend.legendPatch.contains(event)   

    def on_picker(self, event):
        if event.artist == self.legend:
            # left-click
            if event.mouseevent.button == 1:
                self._move_legend(event)

            # mouse button pressed
            if event.mouseevent.button == 2:
                pass

            # right-click
            if event.mouseevent.button == 3:
                self._hideLegend() 

            # mouse up
            if event.mouseevent.button == 'up':
                self._scaleUpLegendFont()

            # mouse down
            if event.mouseevent.button == 'down':
                self._scaleDownLegendFont()
            

    def on_release(self, event):
        if self.gotLegend:
            self.gotLegend = False

    #----------------------------------------------------#
    # Utility functions
               
    def _move_legend(self,event):
            bbox = self.legend.get_window_extent()
            self.mouse_x = event.mouseevent.x
            self.mouse_y = event.mouseevent.y
            self.legend_x = bbox.xmin
            self.legend_y = bbox.ymin 
            self.gotLegend = 1

    def _scaleUpLegendFont(self,size_step=4):
        size = self.legend.get_texts()[0].get_fontsize()
        size += size_step
        _plt.setp(self.legend.get_texts(), fontsize=size) #legend 'list' fontsize
        self.legend.figure.canvas.draw()
         

    def _scaleDownLegendFont(self,size_step=4):
        size = self.legend.get_texts()[0].get_fontsize()
        size -= size_step
        _plt.setp(self.legend.get_texts(), fontsize=size) #legend 'list' fontsize
        self.legend.figure.canvas.draw()

    def _hideLegend(self):
        if self.legend.get_visible():
            self.legend.set_visible(False)
        else:
            self.legend.set_visible(True)
        self.legend.figure.canvas.draw()
            




figure = _plt.figure() 
ax = figure.add_subplot(111)
scatter = ax.scatter(np.random.randn(100), np.random.randn(100), label='hi')
legend = ax.legend()
legend = DraggableLegend(legend)
_plt.show()
