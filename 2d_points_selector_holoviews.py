import numpy as np
import panel as pn
import holoviews as hv
import holoviews.plotting.bokeh

points = hv.Points(np.random.randn(1000,2 )).opts(tools=['box_select', 'lasso_select'])
selection = hv.streams.Selection1D(source=points)


def selected_info(index):
    arr = points.array()[index]
    if index:
        label = 'Mean x, y: %.3f, %.3f' % tuple(arr.mean(axis=0))
    else:
        label = 'No selection'
    return points.clone(arr, label=label).opts(color='red')


layout = points + hv.DynamicMap(selected_info, streams=[selection])

pn.panel(layout).show()
