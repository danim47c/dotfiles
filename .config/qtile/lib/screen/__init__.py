
from libqtile.config import Screen
from libqtile import widget, bar

from .bottom import bottom_widgets
from .top import top_widgets

widget_defaults = dict(
  font='Ubuntu',
  fontsize=14,
  padding=10
)

extension_defaults = widget_defaults.copy()

def screens_func(colors: dict):
  return [
    Screen(
      top=bar.Bar(
        top_widgets(colors),
        30  
      ),
      bottom=bar.Bar(
        bottom_widgets(colors),
        24
      )
    )
  ]



