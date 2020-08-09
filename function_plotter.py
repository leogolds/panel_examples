import holoviews as hv
import numpy as np
import panel as pn


# Create the holoviews app again
def sine(phase):
    xs = np.linspace(0, np.pi * 4)
    return hv.Curve((xs, np.sin(xs + phase))).opts(width=800)


stream = hv.streams.Stream.define('Phase', phase=0.)()
dmap = hv.DynamicMap(sine, streams=[stream])

start, end = 0, np.pi * 2
slider = pn.widgets.FloatSlider(start=start, end=end, value=start, step=0.2, name="Phase")


# Create a slider and play buttons
def animate_update():
    year = slider.value + 0.2
    if year > end:
        year = start
    slider.value = year


def slider_update(event):
    # Notify the HoloViews stream of the slider update
    stream.event(phase=event.new)


slider.param.watch(slider_update, 'value')


def animate(event):
    if button.name == '► Play':
        button.name = '❚❚ Pause'
        callback.start()
    else:
        button.name = '► Play'
        callback.stop()


button = pn.widgets.Button(name='► Play', width=60, align='end')
button.on_click(animate)
callback = button.add_periodic_callback(animate_update, 50, start=False)

app = pn.Column(
    dmap,
    pn.Row(slider, button)
)

app.show()
